from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.main import app

from app.models.riot import RiotId, Puuid
from services.riot_service import get_account_by_riod_id, get_account_by_riot_id, get_matchlist_by_puuid

templates = Jinja2Templates(directory="templates")



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