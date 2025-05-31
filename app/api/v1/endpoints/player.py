from fastapi import APIRouter
from app.models.player import Player
from app.utils import examples
from fastapi import Request, HTTPException

from app.services.api_service import get_matchlist_by_name
from app.utils.grade import calculate_grade
from app.models.riot import RiotId

router = APIRouter()

@router.get("/")
async def player(request: Request):
    match_data = examples.matches_example['data'][0]
    
    all_players = match_data["players"]["all_players"]
    for p in all_players:
        p['first_kills'] = 30
        p['first_deaths'] = 20
    players = [Player.from_dict(p) for p in all_players]

    # Agora você pode iterar e calcular o score de cada jogador:
    for player in players:
        print(f"{player.name} - Score: {player.calculate_score()}")

    return players


@router.post("/grade")
async def player_grade(riot_id: RiotId, mode: str = "competitive"):
    riot_id = riot_id.model_dump()
    match_list = await get_matchlist_by_name(riot_id, mode)
    print(match_list)
    try:
        return calculate_grade(match_list, riot_id)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    
@router.get("/matchlist/{name}/{tag}")
async def matches_matchlist(name: str, tag: str):
    riotid = RiotId(name=name, tag=tag).model_dump()
    match_list = await get_matchlist_by_name(riotid)

    grade = calculate_grade(match_list, riotid)

    return {"match_list": match_list, "grade": grade}
