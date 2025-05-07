from fastapi import APIRouter
from app.api.v1.endpoints import account, item

router = APIRouter()
router.include_router(account.router, prefix="/account", tags=["Players"])
#router.include_router(match.router, prefix="/matches", tags=["Matches"])
router.include_router(item.router, prefix="/items", tags=["Items"])