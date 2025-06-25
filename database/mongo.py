import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def get_mongo_client():
    return MongoClient(os.getenv("MONGO_URI"))

def get_mongo_db():
    client = get_mongo_client()
    return client[os.getenv("MONGO_DB")]
