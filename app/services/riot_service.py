import os
import httpx
from fastapi import FastAPI, Request

from dotenv import load_dotenv

from app.models.riot import RiotId, Puuid


os.environ.pop("API_KEY", None)
load_dotenv()

API_KEY = os.getenv("API_KEY")
app = FastAPI()

URL = "https://americas.api.riotgames.com"

headers = {"X-Riot-Token": API_KEY}


async def get_account_by_riod_id(riotId: RiotId):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/riot/account/v1/accounts/by-riot-id/{riotId.name}/{riotId.tag}?locale=pt-BR", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha ao buscar dados da API externa", "status_code": response.status_code}
    

async def get_account_by_riot_id(puuid: Puuid):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/riot/account/v1/accounts/by-puuid/{puuid.puuid}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha ao buscar dados da API externa", "status_code": response.status_code}


async def get_matchlist_by_puuid(puuid: Puuid):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/val/match/v1/matchlists/by-puuid/{puuid.puuid}", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha ao buscar dados da API externa", "status_code": response.status_code}
    

async def get_content(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha ao buscar dados da API externa", "status_code": response.status_code}