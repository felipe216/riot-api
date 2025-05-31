import os
import httpx
from fastapi import FastAPI, Request

from dotenv import load_dotenv

from app.models.riot import RiotId, Puuid


os.environ.pop("API_2_KEY", None)
load_dotenv()

API_KEY = os.getenv("API_2_KEY")
app = FastAPI()

URL = "https://api.henrikdev.xyz"

headers = {"Authorization": API_KEY}


async def get_matchlist_by_name(riotId: RiotId, mode: str = "competitive"):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/valorant/v4/matches/br/pc/{riotId['name']}/{riotId['tag']}?mode={mode}", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha ao buscar dados da API externa", "status_code": response.status_code}