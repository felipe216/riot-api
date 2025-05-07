import os

from fastapi import FastAPI, Request
import httpx
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from dotenv import load_dotenv

from app.models.riot import RiotId, Puuid
from app.api.v1.api_router import router as api_v1_router
from services.riot_service import get_account_by_riod_id, get_account_by_riot_id, get_matchlist_by_puuid, get_content

templates = Jinja2Templates(directory="templates")

os.environ.pop("API_KEY", None)
load_dotenv()

API_KEY = os.getenv("API_KEY")
app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")

URL = "https://americas.api.riotgames.com"

headers = {"X-Riot-Token": API_KEY}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Página inicial"})


@app.post("/matches/matchlist")
async def matches_matchlist(puuid: Puuid):
    return await get_matchlist_by_puuid(puuid)


@app.get("/skins")
async def content(request: Request):
    return templates.TemplateResponse("content.html", {"request": request, "url": "https://http://127.0.0.1:8000/content/items/"})

@app.get("/items")
async def items(request: Request):
    return templates.TemplateResponse("items.html", {"request": request, "url": "https://http://127.0.0.1:8000/content/items/"})