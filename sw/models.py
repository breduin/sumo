from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, backref

from database import Base


class RikishiBout(Base):
    __tablename__ = 'rikishi_bout'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rikishi_id = Column(Integer, unique=True)
    kaku_id = Column(String(20))
    banzuke_name = Column(String(100))
    banzuke_name_eng = Column(String(100))
    shikona = Column(String(100))
    shikona_eng = Column(String(100))
    won_number = Column(Integer)
    lost_number = Column(Integer)
    rest = Column(String(100))
    rest_eng = Column(String(100))
    result_image = Column(String(100))
    alt = Column(String(100))
    kyokai_member_id = Column(String(100))
    win_lose = Column(String(100))


class BashoDay(Base):
    __tablename__ = 'basho_day'
    id = Column(Integer, primary_key=True)
    TorHtml = Column(String)
    FinHtml = Column(String)
    Result = Column(String)
    dayName = Column(String)
    dayHead = Column(Date)
    dayStr = Column(String)
    kakuName = Column(String)
    PdfUrl = Column(String)
    en = Column(String)
    basho_id = Column(Integer)
    kakuzuke_id = Column(String)
    day = Column(String)
    dispFlg = Column(Integer)


class Bout(Base):
    __tablename__ = 'bout'
    id = Column(Integer, primary_key=True, autoincrement=True)
    judge = Column(Integer)
    technic_name = Column(String(100))
    technic_name_eng = Column(String(100))
    technic_id = Column(Integer)
    east_id = Column(Integer, ForeignKey('rikishi_bout.id'))
    east = relationship(RikishiBout, foreign_keys=[east_id])
    west_id = Column(Integer, ForeignKey('rikishi_bout.id'))
    west = relationship(RikishiBout, foreign_keys=[west_id])
    basho_day_id = Column(Integer, ForeignKey('basho_day.id'))
    basho_day = relationship(BashoDay, foreign_keys=[basho_day_id])
