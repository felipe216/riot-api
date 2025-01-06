import os

from fastapi import FastAPI, Request
import httpx
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from dotenv import load_dotenv

templates = Jinja2Templates(directory="templates")

load_dotenv()

API_KEY = os.getenv("API_KEY")
app = FastAPI()

URL = "https://americas.api.riotgames.com"

headers = {"X-Riot-Token": API_KEY}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Página inicial"})

class RiotId(BaseModel):
    name: str
    tag: str


@app.post("/account/")
async def account(riotid: RiotId):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/riot/account/v1/accounts/by-riot-id/{riotid.name}/{riotid.tag}", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha ao buscar dados da API externa", "status_code": response.status_code}


class Puuid(BaseModel):
    puuid: str

@app.post("/account/by-puuid/")
async def account_by_puuid(puuid: Puuid):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/riot/account/v1/accounts/by-puuid/{puuid.puuid}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha ao buscar dados da API externa", "status_code": response.status_code}