import datetime
from enum import Enum
from typing import Optional, List

from fastapi import Query
from pydantic import BaseModel


class Location(str, Enum):
    All = "All"
    Seoul = "Seoul"
    Gyeonggi = "Gyeonggi"
    Incheon = "Incheon"
    Chungcheong = "Chungcheong"
    Gangwon = "Gangwon"
    Jeolla = "Jeolla"
    Busan = "Busan"
    Jeju = "Jeju"


class Period(str, Enum):
    under = "under"
    over = "over"


class PeriodType(str, Enum):
    week = "week"
    month = "month"


class ApplyItem(BaseModel):
    homeNumber: int
    roomId: int
    name: str = Query(title="이름" )
    phone: str = Query(title="휴대폰번호", regex="^(01[0,1,6,7,8,9]{1})-([0-9]{3,4})-([0-9]{4})$")
    email: str = Query(title="Email주소", regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    apply_privacy: str = Query(title="개인정보 동의 여부 ")
    startDate: datetime.date = Query(title="입주일 ")
    endDate: datetime.date = Query(title="만료일 ")

    class Config:
        schema_extra = {
                "homeNumber": 1,
                "roomId": 2,
                "name": "홍길동",
                "phone": "010-1111-1111",
                "email": "test@test.com",
                "apply_privacy": "Y",
                "startDate": "2023-02-16",
                "endDate": "2023-03-16"
        }



class Room(BaseModel):
    roomId: int
    roomName: str
    deposit: int
    rent: int
    periodType: PeriodType


class HomeItem(BaseModel):
    homeNumber: int
    title: str
    contents: str
    rooms: Optional[List[Room]] = None
    options: Optional[List[str]] = None
    startDate: datetime.date = Query(title="입주 가능일 ")
    location: Location
    period: Period
