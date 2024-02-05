# app/config/connect.py

import aiomysql
from databases import Database
from fastapi import HTTPException

async def connect_db():
    try:
        db = Database("mysql+aiomysql://user:password@localhost/dbname")
        await db.connect()
        return db
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

async def close_conn(db):
    try:
        await db.disconnect()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error closing database connection: {str(e)}")
