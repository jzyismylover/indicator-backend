from flask_restful import request, output_json
import datetime
import jwt

SALT = '%INDICATOR_BACKEND%'

def create_token(username, password):
    payload = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
    }
    token = jwt.encode(payload=payload, key=SALT, algorithm='HS256')

    return token


def verify_token(token):
    msg = None
    try:
        # based on Bearer token
        token = token[8:]
        jwt.decode(token, key=SALT, algorithms='HS256')
        status = 200
    except Exception as e:
        status = 201
        msg = str(e)

    return {
        'msg': msg,
        'status': status
    }

def check_premission():
    headers = request.headers
    token = headers.environ['HTTP_AUTHORIZATION'][7:]
    auth = verify_token(token)
    if auth['status'] == 200:
        return None
    else:
        return output_json({
            'data': {
                'msg': auth['msg']
            }
        }, auth['status'])

if __name__ == '__main__':
    username = 'jzyismylover'
    password = 'HSHAHAHA'
    print(create_token(username, password))

    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imp6eWlzbXlsb3ZlciIsInBhc3N3b3JkIjoiSFNIQUhBSEEiLCJleHAiOjE2Nzc4MzE2ODR9.90qBWzUlPJcbM8XM_aABF80LUSMvKBNVHW7VMbe2fYM'
    ans = verify_token(token)
    print(ans)