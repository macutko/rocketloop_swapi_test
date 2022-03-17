from typing import List

from fastapi import APIRouter, Depends, Query
from starlette.testclient import Params

from auth.auth import get_current_user
from lib.sanitizers import Sanitizers
from lib.swapi_service import SwapiService, Person

router = APIRouter(
    prefix="/api/v1/people",
    tags=["people"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Person])
async def people(page: int = Query(None)):
    ppl = SwapiService().get_people(1 if page is None else page)

    if ppl['next'] is not None:
        ppl['next'] = Sanitizers.url(ppl['next'])
    del ppl['count']

    return Sanitizers.people(ppl['results'])


@router.get("/{person_id}")
async def person(person_id: int):
    return SwapiService().get_people(person_id)

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
