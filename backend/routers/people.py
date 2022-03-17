from enum import Enum
from typing import List

from fastapi import APIRouter, Depends, Query
from fastapi.params import Param

from auth.auth import get_current_user
from lib.swapi import Swapi, Person

router = APIRouter(
    prefix="/api/v1/people",
    tags=["people"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


class FilterTypes(str, Enum):
    films: str = "film"
    name: str = "name"


@router.get("/{filter_name}", response_model=List[Person])
async def people(filter_name: str = Param(...), query: List[str] = Query(...), page: int = Query(None)):
    all_people = Swapi().get_poeple(1 if page is None else page)

    res = []
    for person in all_people["results"]:
        for q in query:
            if q in person[filter_name]:
                res.append(person)

    return list({v['name']: v for v in res}.values())
