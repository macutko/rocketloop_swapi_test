from enum import Enum
from typing import List

from fastapi import APIRouter, Depends, Query

from auth.auth import get_current_user
from lib.swapi import Swapi

router = APIRouter(
    prefix="/api/v1/people",
    tags=["people"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


class FilterTypes(str, Enum):
    films: str = "film"
    name: str = "name"


@router.get("/")
async def people(filter: List[str] = Query(...)):
    all_people = Swapi().get_poeple()

    # for (query in request.query_params)

    return {"test": "here"}
