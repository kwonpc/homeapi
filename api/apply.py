from fastapi import APIRouter
from db import config
from schema import items

router = APIRouter(
    prefix="/apply",
    tags=["apply"]
)


@router.put("/", description="입주 문의 신청 API")
async def apply(item_request: items.ApplyItem,
                examples={
                          "homeNumber": "매물번호",
                          "roomId": "룸번호",
                          "name": "이름",
                          "phone": "휴대폰 번호 010-1111-1111",
                          "email": "이메일 주소 test@test.com",
                          "apply_privacy": "개인정보 동의 여부 Y/N",
                          "startDate": "입주일 2023-02-16",
                          "endDate": "만료일 2023-03-16"
                        }
                ):
    apply_collection = config.client.home.apply
    apply_item_dict = item_request.dict()

    if item_request.startDate:
        apply_item_dict.update({"startDate": item_request.startDate.isoformat()})
    if item_request.endDate:
        apply_item_dict.update({"endDate": item_request.endDate.isoformat()})

    apply_collection.insert_one(apply_item_dict)

    return item_request
