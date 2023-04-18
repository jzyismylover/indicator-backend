import time
import pickle
import os
from flask_redis import FlaskRedis

def get_redis_path():
    if os.path.exists('/.dockerenv'):
        password = os.environ['REDIS_PASSWORD']
        hostname = os.environ['REDIS_HOSTNAME']
        redis_path = f'redis://:{password}@{hostname}'
    else:
        password = os.environ['REDIS_PASSWORD']
        hostname = os.environ['REDIS_HOSTNAME']
        port = os.environ['REDIS_PORT']
        redis_path = f'redis://:{password}@{hostname}:{port}'
    
    return redis_path

def init_redis(app) -> FlaskRedis:
    redis_path  = get_redis_path()
    app.config['REDIS_URL'] = redis_path
    return FlaskRedis(app)


KEY = 'indicator%'
def mark_dyn_data(id, data, expire=3600):
    # store redis data
    from setup import redis_client

    user_id = str(id)
    data = pickle.dumps(data)
    expires = int(time.time()) + expire
    data_key = KEY + user_id
    try:
        p = redis_client.pipeline()
        p.set(data_key, data)
        p.expireat(data_key, expires)
        p.execute()
    except Exception as e:
        pass


def get_dyn_data(id):
    # get redis data
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


def delete_dyn_data(id):
    # delete redis data
    from setup import redis_client

    id = str(id)
    data_key = KEY + id
    try:
        redis_client.delete(data_key)
    except:
        pass
