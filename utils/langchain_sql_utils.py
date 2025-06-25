import os
import urllib.parse
from dotenv import load_dotenv
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_openai import ChatOpenAI

load_dotenv()

def get_sql_chain():
    # URL-encode password for SQLAlchemy URI
    password = urllib.parse.quote_plus(os.getenv('MYSQL_PASSWORD'))
    mysql_uri = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{password}"
        f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
    )
    db = SQLDatabase.from_uri(mysql_uri)
    llm = ChatOpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
        model=os.getenv("GROQ_MODEL", "llama3-8b-8192"),
        temperature=0
    )
    chain = create_sql_query_chain(llm, db)
    return chain, llm

def ask_sql_db(question: str):
    import re
    from database.mysql import get_mysql_connection

    chain, llm = get_sql_chain()
    result = chain.invoke({"question": question})

    # Extract the SQL query from the result string
    match = re.search(r'SQLQuery:\s*(.*)', result)
    sql_query = match.group(1) if match else None

    if not sql_query:
        return {"answer": "Sorry, I could not generate a valid SQL query for your question."}

    # Run the SQL query on the transactions table
    conn = get_mysql_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
    except Exception as e:
        return {"answer": f"SQL execution error: {str(e)}"}
    finally:
        conn.close()

    if not rows:
        return {"answer": "No data found for your query."}

    # Limit the number of rows shown to the LLM for summarization
    MAX_ROWS = 20
    display_rows = rows[:MAX_ROWS]
    more_rows = len(rows) - MAX_ROWS if len(rows) > MAX_ROWS else 0

    # Format the data for the LLM prompt
    context = (
        f"Here is a list of transaction records from a wealth management database:\n"
        f"{display_rows}\n"
    )
    if more_rows:
        context += f"...and {more_rows} more rows not shown.\n"
    context += (
        f"Based on this data, answer the following business question in clear, concise natural language for a finance executive:\n"
        f"Question: {question}\n"
        f"Answer:"
    )

    # Ask the LLM to summarize the data
    try:
        answer = llm.invoke(context)
    except Exception as e:
        return {"answer": f"LLM error: {str(e)}"}

    return {"answer": answer}
