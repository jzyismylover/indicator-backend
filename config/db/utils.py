from config.db import engine
from sqlalchemy import select
from sqlalchemy.orm import Session

def getSQLData(stmt):
  with Session(engine) as session:
    rows = session.execute(stmt)
    for row in rows:
      print(row)

def updateSQLData():
  pass

def deleteSQLData():
  pass

def patchSQLData():
  pass