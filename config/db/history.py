# 历史记录表(存储file文件)
from sqlalchemy import (
  Column,
  Integer,
  ForeignKey,
  Text,
  String
)

from config.db import Base
class History(Base):
  __tablename__ = 'history'
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  content = Column(Text, nullable=False)
  type = Column(String(10), nullable=False)