from sqlalchemy import BigInteger, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id = Column(BigInteger, primary_key=True)
