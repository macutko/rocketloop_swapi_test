from fastapi import APIRouter, Depends
from pydantic import BaseModel

from auth.auth import AuthHandler
from lib.sanitizers import Sanitizers
from lib.swapi_service import SwapiService

router = APIRouter(
    prefix="/api/v1/species",
    tags=["species"],
    dependencies=[Depends(AuthHandler().get_current_user)],
    responses={404: {"description": "Not found"}},
)


class SpecieResponse(BaseModel):
    name: str


@router.get("/{specie_id}", response_model=SpecieResponse)
async def get_specie_by_id(specie_id: int):
    return Sanitizers.specie(SwapiService().get_specie(specie_id))
