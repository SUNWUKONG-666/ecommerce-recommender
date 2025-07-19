from dotenv import load_dotenv
import os
import mysql.connector

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("sql12.freesqldatabase.com"),
        user=os.getenv("sql12790810"),
        password=os.getenv("MgP3LnRLQK"),
        database=os.getenv("sql12790810"),
        port=int(os.getenv("DB_PORT", 3306))
    )