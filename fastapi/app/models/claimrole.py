from app.config.connect import connect_db, close_conn

async def get_claimrole(username: str):
    try:
        conn = await connect_db()
        query = """
        SELECT * 
        FROM claimoccurrence_userrole 
        WHERE lower(username) = lower(:username);
        """
        result = await conn.execute(query, {"username": username})
        return result.fetchall()
    finally:
        await close_conn(conn)
