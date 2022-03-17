from fastapi import APIRouter, Depends
from pydantic import BaseModel

from auth.auth import get_current_user
from lib.sanitizers import Sanitizers
from lib.swapi_service import SwapiService

router = APIRouter(
    prefix="/api/v1/species",
    tags=["species"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


class StarshipResponse(BaseModel):
    name: str


@router.get("/{starship_id}", response_model=StarshipResponse)
async def get_starship_by_id(starship_id: int):
    return Sanitizers.starship(SwapiService().get_starship(starship_id))
