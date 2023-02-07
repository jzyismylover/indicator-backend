from sqlalchemy import (
    Column,
    Integer,
    String,
    UniqueConstraint,
    Index,
    DATETIME,
    ForeignKey,
)
from config import db

# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(32), unique=True, nullable=False)
