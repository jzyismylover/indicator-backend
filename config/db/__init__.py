import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from yaml import safe_load

# yml 配置文件
FILE_NAME = os.path.abspath(os.path.join('config', 'config.yml'))
with open(FILE_NAME, 'rb') as f:
    try:
        y = safe_load(f)
    except Exception as e:
        pass

# mysql 区分开发、生产环境
if os.path.exists('/.dockerenv'):
    config = {
        'username': os.environ['MYSQL_USERNAME'],
        'hostname': os.environ['MYSQL_HOSTNAME'],
        'port': os.environ['MYSQL_PORT'],
        'password': os.environ['MYSQL_PASSWORD'],
        'dbname': os.environ['MYSQL_DBNAME'],
    }
else:
    config = y['de_db']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    config['username'],
    config['password'],
    config['hostname'],
    config['port'],
    config['dbname'],
)

# orm 引擎(懒初始化)
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=True,
    future=True,
    pool_recycle=3600,
    pool_pre_ping=True,
)
# orm query
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
# 数据模型基类
Base = declarative_base()
# 基类添加 orm query
Base.query = db_session.query_property()


def init_db():
    # 函数中 import 对应的数据模型统一使用 create_all 创建
    import config.db.user
    import config.db.history

    Base.metadata.create_all(bind=engine)
