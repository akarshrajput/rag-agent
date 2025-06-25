import os
import pymysql
from dotenv import load_dotenv
from pymysql.cursors import DictCursor

load_dotenv()

def get_mysql_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        cursorclass=DictCursor
    )
