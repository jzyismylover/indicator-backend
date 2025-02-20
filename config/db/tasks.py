from sqlalchemy import (
  Column, 
  Integer, 
  Text, 
  String,
  ForeignKey
)
from config.db import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String(50), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    update_time = Column(String(20))
    result = Column(Text)