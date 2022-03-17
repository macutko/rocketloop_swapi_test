from fastapi import APIRouter, Depends, Request

from auth.auth import get_current_user

router = APIRouter(
    prefix="/api/v1/people",
    tags=["people"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_people(request: Request):
    print(request.query_params)
    return {"test": "here"}
