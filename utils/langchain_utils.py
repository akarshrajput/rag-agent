import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def ask_openai(message: str):
    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    response = llm([HumanMessage(content=message)])
    return response.content
