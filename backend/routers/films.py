from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from auth.auth import get_current_user
from lib.sanitizers import Sanitizers
from lib.swapi_service import SwapiService

router = APIRouter(
    prefix="/api/v1/films",
    tags=["films"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


class Film(BaseModel):
    title: str


@router.get("/", response_model=List[Film])
async def get_all_films():
    return Sanitizers.films(SwapiService().get_films()["results"])


@router.get("/{film_id}", response_model=Film)
async def get_film_by_id(film_id: int):
    return Sanitizers.film(SwapiService().get_film(film_id))
