from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, MetaData, text
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from datetime import datetime

import urllib.parse
from fastapi.responses import JSONResponse

encoded_password = urllib.parse.quote("password123123")
DATABASE_URL = f"postgresql://userpanupong:{encoded_password}@172.x.x.x/occ_dbname"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS Configuration
origins = [
    "http://localhost:8080",  # Add other allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/test")
def read_root():
    return {"message": "Hello, FastAPI with PostgreSQL!"}

@app.get("/now")
def read_current_time(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT NOW()")).first()
    return {"current_time": result[0]}

@app.get("/data/part_all")
def read_data_part():
    data = [
        { 'name': 'Part A', 'parts': [{ 'name': 'Part A', 'value': '' }, { 'name': 'Part B', 'value': '3' }, { 'name': 'Part C', 'value': '4' }], 'editTime': '' },
        { 'name': 'Part B', 'parts': [{ 'name': 'Part A', 'value': '4' }, { 'name': 'Part B', 'value': '' }, { 'name': 'Part C', 'value': '2' }], 'editTime': '' },
        { 'name': 'Part C', 'parts': [{ 'name': 'Part A', 'value': '5' }, { 'name': 'Part B', 'value': '6' }, { 'name': 'Part C', 'value': '' }], 'editTime': '' },
    ]
    return JSONResponse(content=data, headers={"Access-Control-Allow-Origin": "http://localhost:8080"})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
