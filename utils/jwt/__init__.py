import datetime
import jwt
import re

SALT = '%INDICATOR_BACKEND%'

def create_token(username, password):
    payload = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
    }
    token = jwt.encode(payload=payload, key=SALT, algorithm='HS256')

    return 'Bearer ' + token


def verify_token(token) -> bool:
    msg = None
    try:
        status = jwt.decode(token, key=SALT, algorithms='HS256')
    except Exception as e:
        status = 201
        msg = e

    return {
        'msg': msg,
        'status': status
    }


if __name__ == '__main__':
    username = 'jzyismylover'
    password = 'HSHAHAHA'
    print(create_token(username, password))

    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imp6eWlzbXlsb3ZlciIsInBhc3N3b3JkIjoiSFNIQUhBSEEiLCJleHAiOjE2Nzc2NzIzNDV9.UFS8s-X26CjI57U78x7cli_qNNh9WLFVclAdN2K0aD'
    ans = verify_token(token)
    print(ans)