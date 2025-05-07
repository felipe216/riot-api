from fastapi import APIRouter
from app.models.riot import Puuid
from app.services.riot_service import get_matchlist_by_puuid

router = APIRouter()


@router.post("/matchlist")
async def matches_matchlist(puuid: Puuid):
    return await get_matchlist_by_puuid(puuid)