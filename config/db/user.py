from sqlalchemy import (
    Column,
    Integer,
    String,
    UniqueConstraint,
    Index,
    DATETIME,
    ForeignKey,
)
from config.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.username = password
