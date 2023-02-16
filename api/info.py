from fastapi import APIRouter
from starlette.responses import JSONResponse

from db import config

router = APIRouter(
    prefix="/info",
    tags=["info"]
)


@router.get("/{homeNumber}")
async def info(homeNumber: int):
    home_collection = config.client.home.home
    home = home_collection.find_one({"homeNumber": homeNumber}, {'_id': 0})

    if home:
        return dict(home)
    else:
        return JSONResponse(status_code=404, content='data not found')


