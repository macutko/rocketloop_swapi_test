from typing import List

from fastapi import APIRouter, Depends

from auth.auth import get_current_user
from lib.sanitizers import Sanitizers
from lib.swapi_service import SwapiService, Person

router = APIRouter(
    prefix="/api/v1/species",
    tags=["species"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{specie_id}")
async def people(specie_id: int):
    specie = SwapiService().get_specie(specie_id)
    return Sanitizers.specie(specie)
