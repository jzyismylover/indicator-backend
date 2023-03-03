import time
import pickle
import os
from flask_redis import FlaskRedis
from yaml import safe_load

FILE_NAME = os.path.abspath(os.path.join('config', 'config.yml'))
with open(FILE_NAME, 'rb') as f:
    try:
        y = safe_load(f)
    except Exception as e:
        pass


def init_redis(*, app) -> FlaskRedis:
    if os.path.exists('/.dockerenv'):
        hostname, port = y['pd_redis'].values()
        redis_path = f'redis://{hostname}:{port}'
    else:
        hostname, port, password = y['de_redis'].values()
        redis_path = f'redis://{password}:@{hostname}:{port}'
    app.config['REDIS_URL'] = redis_path
    return FlaskRedis(app)


KEY = 'indicator%'


def mark_dyn_data(id, data):
    from setup import redis_client

    user_id = str(id)
    data = pickle.dumps(data)
    expires = int(time.time()) + 3600
    data_key = KEY + user_id
    try:
        p = redis_client.pipeline()
        p.set(data_key, data)
        p.expireat(data_key, expires)
        p.execute()
    except Exception as e:
        pass


def get_dyn_data(id):
    from setup import redis_client

    id = str(id)
    data_key = KEY + id
    try:
        data = redis_client.get(data_key)
    except Exception as e:
        return None

    if data:
        return pickle.loads(data)
    return None
