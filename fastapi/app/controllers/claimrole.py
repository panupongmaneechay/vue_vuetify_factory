from app.models.claimrole import get_claimrole

async def get_claimrole(username: str):
    try:
        result = await get_claimrole(username)
        return {"status": True, "message": "Query Success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
