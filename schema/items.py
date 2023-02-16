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
    name: str = Query(title="이름 ")
    phone: str = Query(title="휴대폰번호", regex="^\\+?[1-9][0-9]{7,14}$")
    email: str = Query(title="Email주소", regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    apply_privacy: str = Query(title="개인정보 동의 여부 ")
    startDate: datetime.date = Query(title="입주일 ")
    endDate: datetime.date = Query(title="만료일 ")


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



