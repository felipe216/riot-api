from fastapi import APIRouter
from app.models.riot import Puuid, RiotId
from app.services.riot_service import get_matchlist_by_puuid
from app.services.api_service import get_matchlist_by_name
from app.utils.grade import calculate_grade

router = APIRouter()


@router.post("/matchlist")
async def matches_matchlist(riotid: RiotId):
    return await get_matchlist_by_name(riotid)