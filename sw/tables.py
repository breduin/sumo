from sqlalchemy import Table, Column, Integer, String, ForeignKey
from database import Base


metadata = Base.metadata


rikishi_bout_table = Table(
    'rikishi_bout',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('rikishi_id', Integer),
    Column('kaku_id', String(20)),
    Column('banzuke_name', String(100)),
    Column('banzuke_name_eng', String(100)),
    Column('shikona', String(100)),
    Column('shikona_eng', String(100)),
    Column('won_number', Integer),
    Column('lost_number', Integer),
    Column('rest', String(100)),
    Column('rest_eng', String(100)),
    Column('result_image', String(100)),
    Column('alt', String(100)),
    Column('kyokai_member_id', String(100)),
    Column('win_lose', String(100))
)


bout_table = Table(
    'bout',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('judge', Integer),
    Column('technic_name', String(100)),
    Column('technic_name_eng', String(100)),
    Column('technic_id', Integer),
    Column('east_id', Integer, ForeignKey('rikishi.id')),
    Column('west_id', Integer, ForeignKey('rikishi.id')),
)


basho_day_table = Table(
    'basho_day',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('TorHtml', String),
    Column('FinHtml', String),
    Column('Result', String),
    Column('dayName', String),
    Column('dayHead', String),
    Column('dayStr', String),
    Column('kakuName', String),
    Column('PdfUrl', String),
    Column('en', String),
    Column('basho_id', Integer),
    Column('kakuzuke_id', String),
    Column('day', String),
    Column('dispFlg', Integer),
)
