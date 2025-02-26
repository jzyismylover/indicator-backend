from sqlalchemy import Column, Integer, String, ForeignKey
from config.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    appid = Column(String(255))
