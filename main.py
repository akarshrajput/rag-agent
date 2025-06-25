from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crud.mysql_crud import get_users, add_user, get_transactions, add_transaction
from crud.mongo_crud import get_clients, add_client
from utils.langchain_sql_utils import ask_sql_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Your Next.js frontend origin
    # Add more origins if needed, e.g. production frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # use ["*"] to allow all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running"}

# MySQL User endpoints
@app.get("/users")
def read_users():
    try:
        return get_users()
    except Exception as e:
        print("Error in /users:", e)
        raise HTTPException(status_code=500, detail=str(e))

class UserCreate(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    try:
        user_id = add_user(user.name, user.age)
        return {"id": user_id, "name": user.name, "age": user.age}
    except Exception as e:
        print("Error in /users POST:", e)
        raise HTTPException(status_code=500, detail=str(e))

# MySQL Transaction endpoints
class TransactionCreate(BaseModel):
    client_name: str
    stock_name: str
    stock_symbol: str
    transaction_type: str  # 'buy' or 'sell'
    quantity: int
    price_per_unit: float
    total_value: float
    transaction_date: str  # 'YYYY-MM-DD'
    relationship_manager: str

@app.get("/transactions")
def read_transactions():
    try:
        return get_transactions()
    except Exception as e:
        print("Error in /transactions:", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/transactions")
def create_transaction(tx: TransactionCreate):
    try:
        tx_id = add_transaction(
            tx.client_name,
            tx.stock_name,
            tx.stock_symbol,
            tx.transaction_type,
            tx.quantity,
            tx.price_per_unit,
            tx.total_value,
            tx.transaction_date,
            tx.relationship_manager
        )
        return {"id": tx_id, **tx.dict()}
    except Exception as e:
        print("Error in /transactions POST:", e)
        raise HTTPException(status_code=500, detail=str(e))

# MongoDB endpoints
@app.get("/clients")
def read_clients():
    try:
        return get_clients()
    except Exception as e:
        print("Error in /clients:", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/clients")
def create_client(client: dict):
    try:
        client_id = add_client(client)
        return {"id": client_id}
    except Exception as e:
        print("Error in /clients POST:", e)
        raise HTTPException(status_code=500, detail=str(e))

# LangChain SQL QA endpoint (Groq LLM)
class SQLQueryRequest(BaseModel):
    question: str

@app.post("/sql-qa")
def sql_qa(request: SQLQueryRequest):
    try:
        result = ask_sql_db(request.question)
        return result
    except Exception as e:
        print("Error in /sql-qa:", e)
        raise HTTPException(status_code=500, detail=str(e))
