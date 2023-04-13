import datetime
import jwt
from flask_restful import request, abort
from utils.json_response import make_error_response
from config.redis import get_dyn_data

SALT = '%INDICATOR_BACKEND%'

def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24), # 时间变化导致每次生成token签名不一样
    }
    token = jwt.encode(payload=payload, key=SALT, algorithm='HS256')

    return token


def verify_token(token):
    msg = None
    try:
        # based on Bearer token
        token = token
        info = jwt.decode(token, key=SALT, algorithms='HS256')
        status = 200
    except Exception as e:
        status = 401
        msg = str(e)
        info = None

    return {'msg': msg, 'status': status, 'info': info}


def check_premission(fn):
    # @wraps(fn)  # 更新函数 __name__ 签名
    def wrapper(self, *args, **kwargs):
        headers = request.headers
        if 'HTTP_AUTHORIZATION' not in headers.environ:
            return abort(401, **make_error_response(msg='缺少 token字段'))
        token = headers.environ['HTTP_AUTHORIZATION'][7:]
        if get_dyn_data(token) is not None:
            # token黑名单
            return abort(401, **make_error_response(msg='该token已销毁, 请重新登陆'))
        auth = verify_token(token)
        if auth['status'] == 200:
            return fn(self, auth['info'], *args, **kwargs)
        else:
            return abort(401, **make_error_response(msg=auth['msg']))

    return wrapper