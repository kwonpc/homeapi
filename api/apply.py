from fastapi import APIRouter
from db import config
from schema import items

router = APIRouter(
    prefix="/apply",
    tags=["apply"]
)


@router.put("/")
async def apply(item_request: items.ApplyItem):
    apply_collection = config.client.home.apply
    apply_item_dict = item_request.dict()

    if item_request.startDate:
        apply_item_dict.update({"startDate": item_request.startDate.isoformat()})
    if item_request.endDate:
        apply_item_dict.update({"endDate": item_request.endDate.isoformat()})

    apply_collection.insert_one(apply_item_dict)

    return item_request
