from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel

from auth.auth import get_current_user
from lib.custom_typings import URL
from lib.sanitizers import Sanitizers
from lib.swapi_service import SwapiService

router = APIRouter(
    prefix="/api/v1/people",
    tags=["people"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


class Person(BaseModel):
    name: Optional[Optional[str]]
    films: Optional[List[URL]]
    species: Optional[List[URL]]
    starships: Optional[List[URL]]


class PersonResponse(BaseModel):
    next: URL
    results: List[Person]


@router.get("/", response_model=PersonResponse)
async def get_all_people(page: int = Query(None)):
    ppl = SwapiService().get_people(1 if page is None else page)

    return {"next": ppl['next'], "results": Sanitizers.people(ppl['results'])}

#
# @router.get("/{person_id}")
# async def get_person(person_id: int):
#     return SwapiService().get_people(person_id)

# @router.get("/{filter_name}", response_model=List[Person])
# async def people(filter_name: str = Param(...), query: List[str] = Query(...), page: int = Query(None)):
#     all_people = SwapiService().get_people(1 if page is None else page)
#
#     res = []
#     for person in all_people["results"]:
#         for q in query:
#             if q in person[filter_name]:
#                 res.append(person)
#
#     return list({v['name']: v for v in res}.values())
