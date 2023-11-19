import datetime
from pydantic import BaseModel
from typing import List


class RikishiBout(BaseModel):
    rikishi_id: int = None
    kaku_id: str = None
    banzuke_name: str = None
    banzuke_name_eng: str = None
    shikona: str = None
    shikona_eng: str = None
    won_number: int = None
    lost_number: int = None
    rest: str = None
    rest_eng: str = None
    result_image: str = None
    alt: str = None
    kyokai_member_id: str = None
    win_lose: str = None


class Bout(BaseModel):
    judge: int = None
    technic_name: str = None
    technic_name_eng: str = None
    technic_id: int = None


class BashoDay(BaseModel):
    TorHtml: str = None
    FinHtml: str = None
    Result: str = None
    dayName: str = None
    dayHead: datetime.date = None
    dayStr: str = None
    kakuName: str = None
    PdfUrl: str = None
    en: str = None
    basho_id: int = None
    kakuzuke_id: str = None
    day: str = None
    dispFlg: int = None
