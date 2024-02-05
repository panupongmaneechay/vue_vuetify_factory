from fastapi import FastAPI, HTTPException
from app.api.routes import claimrole
from app.models.claimrole import get_claimrole
from app.config.connect import connect_db, close_conn

app = FastAPI()

@app.get("/claimrole/get")
async def get_claimrole(username: str):
    try:
        conn = await connect_db()
        result = await get_claimrole(conn, username)
        return {"status": True, "message": "Query Success", "data": result}
    except HTTPException as e:
        return {"status": False, "err": str(e)}
    finally:
        await close_conn(conn)
