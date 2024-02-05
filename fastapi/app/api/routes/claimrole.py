from fastapi import APIRouter
from app.controllers.claimrole import get_claimrole

router = APIRouter()

@router.get("/claimrole/get")
async def get_claimrole(username: str):
    return await get_claimrole(username)
