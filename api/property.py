import datetime
from typing import Optional
from fastapi import APIRouter, Query
from starlette.responses import JSONResponse

from db import config
from schema import items

router = APIRouter(
    prefix="/property",
    tags=["property"]
)


@router.get("/{location}/{period}", description="매물 리스트 조회 API")
async def property(location: items.Location, period: items.Period, date: Optional[datetime.date] = None):

    req = {"location": location, "period": period}
    if location.value == "All":
        del(req['location'])
    if date:
        req.update({"startDate": {"$lte": date.isoformat()}})

    home_collection = config.client.home.home
    homes = list(home_collection.find(req, {'_id': 0}))
    print(homes)
    if homes:
        return homes
    else:
        return JSONResponse(status_code=404, content='data not found')

