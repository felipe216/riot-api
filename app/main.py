import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from dotenv import load_dotenv

from app.api.v1.api_router import router as api_v1_router

templates = Jinja2Templates(directory="templates")

os.environ.pop("API_KEY", None)
load_dotenv()

API_KEY = os.getenv("API_KEY")
app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")
