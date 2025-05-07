from fastapi import APIRouter
from app.models.riot import RiotId, Puuid
from app.services.riot_service import get_account_by_riod_id, get_account_by_riot_id

router = APIRouter()

@router.post("/account/")
async def account(riotid: RiotId):
    return await get_account_by_riod_id(riotid)


@router.post("/account/by-puuid/")
async def account_by_puuid(puuid: Puuid):
    return await get_account_by_riot_id(puuid)