from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


async_engine = create_async_engine('sqlite+aiosqlite:///sumodb.db', echo=True)
async_session = sessionmaker(async_engine, class_=AsyncSession)

Base = declarative_base()
