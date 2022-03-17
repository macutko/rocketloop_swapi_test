from typing import List

from fastapi import APIRouter, Depends
from fastapi.params import Param

from auth.auth import get_current_user
from lib.swapi_service import SwapiService, Person

router = APIRouter(
    prefix="/api/v1/species",
    tags=["species"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{specie_id}", response_model=List[Person])
async def people(specie_id: str = Param(None)):
    all_people = SwapiService().get_people(1 if page is None else page)

    res = []
    for person in all_people["results"]:
        for q in query:
            if q in person[filter_name]:
                res.append(person)

    return list({v['name']: v for v in res}.values())
