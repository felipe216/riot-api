from fastapi import APIRouter
from app.models.player import Player
from app.utils import examples
from fastapi import Request

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