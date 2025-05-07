from fastapi import APIRouter

from app.api.v1.endpoints import templates

router = APIRouter()


router.include_router(templates.router, tags=["Templates"])