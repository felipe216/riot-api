from fastapi import APIRouter
from app.services.riot_service import get_content
from fastapi import Request

router = APIRouter()

@router.get("/content/items")
async def content(request: Request):
    URLC = "https://br.api.riotgames.com"
    return await get_content(URLC)