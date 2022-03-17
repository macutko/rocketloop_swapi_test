from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel

from auth.auth import AuthHandler
from lib.custom_typings import URL
from lib.sanitizers import Sanitizers
from lib.swapi_service import SwapiService

router = APIRouter(
    prefix="/api/v1/people",
    tags=["people"],
    dependencies=[Depends(AuthHandler().get_current_user)],
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


@router.get("/{filter_name}", response_model=PersonResponse)
async def people(filter_name: str, query: List[str] = Query(...), page: int = Query(None)):
    ppl = SwapiService().get_people(1 if page is None else page)
    next_page = ppl["next"]
    ppl = Sanitizers.people(ppl["results"])

    res = []
    for person in ppl:
        for q in query:
            if q in person[filter_name]:
                res.append(person)

    print(list({v['name']: v for v in res}.values()))
    return {"next": next_page, "results": list({v['name']: v for v in res}.values())}
