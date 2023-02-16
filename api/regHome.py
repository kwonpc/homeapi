from fastapi import APIRouter
from db import config
from schema import items

router = APIRouter(
    prefix="/reg",
    tags=["regist home"]
)


@router.put("/")
async def regHome(item_request: items.HomeItem):
    home_collection = config.client.home.home
    home_item_dict = item_request.dict()

    if item_request.startDate:
        home_item_dict.update({"startDate": item_request.startDate.isoformat()})

    home_collection.insert_one(home_item_dict)

    return item_request
