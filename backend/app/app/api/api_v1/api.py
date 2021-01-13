from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, adverts

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(users.router, prefix="/adverts", tags=["adverts"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
