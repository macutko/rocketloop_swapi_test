from fastapi import APIRouter, Depends

from auth.auth import get_current_user
from lib.swapi import Swapi

router = APIRouter(
    prefix="/api/v1/films",
    tags=["films"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_films():
    return Swapi().get_films()
