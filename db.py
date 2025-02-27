from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///taskmanager.db', echo=True)

SessionLocal = sessionmaker(bing=engine)


class Base(DeclarativeBase):
    pass

# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)