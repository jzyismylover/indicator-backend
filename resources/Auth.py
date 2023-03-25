import re
import hashlib
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, request
from utils.jwt import create_token
from config.mail import sendCaptcha, verifyCaptcha
from config.db import engine
from config.db.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from utils.json_response import make_success_response, make_error_response

def generate_hash_password(password, value='indicator'):
    # value 作为混淆字符串
    sha256 = hashlib.sha256(password.encode("utf-8"))
    sha256.update(value.encode("utf-8"))
    password_sha256 = sha256.hexdigest()
    return password_sha256


def verify_passwd(value, name):
    ans = re.search(
        '^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]{5,20}$',
        value,
    )
    if ans is None:
        raise ValueError('密码需满足至少8位且包含数字大小写字母以及特殊字符')
    else:
        return value


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True, location='form')
login_parser.add_argument(
    'password', type=verify_passwd, required=True, location='form'
)


class UsernameBasedLogin(Resource):
    def post(self):
        params = login_parser.parse_args()
        # username unique / so the following results length assert equal to 1
        username, password = params['username'], params['password']
        try:
            with engine.connect() as conn:
                results = conn.execute(select(User).where(User.username == username))
                results = list(results)
                if len(results) == 0:
                    return make_error_response(msg='用户名不存在'), 400
                if password != results[0]['password']:
                    return make_error_response(msg='密码不正确'), 400
        except Exception as e:
            print(e)
            pass

        token = create_token(username, password)
        return {'data': {'token': token}}, 200


class EmailBasedLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, location='form')
        parser.add_argument('password', required=True, location='form')
        params = parser.parse_args()
        email, password = params['email'], params['password']
        try:
            with engine.connect() as conn:
                results = conn.execute(select(User).where(User.email == email))
                results = list(results)
                if len(results) == 0:
                    return make_error_response(msg='邮箱不存在'), 400
                if password != results[0]['password']:
                    return make_error_response(msg='密码不正确'), 400
        except:
            pass
            
        token = create_token(email, password)
        return make_success_response(data={
            'token': token
        }, msg='登录成功'), 200


class Regist(Resource):
    def post(self):
        regist_parser = login_parser.copy()
        regist_parser.add_argument('email', required=True, location='form')
        regist_parser.add_argument('code', required=True, location='form')
        params = regist_parser.parse_args()
        username, password, email, code = (
            params['username'],
            params['password'],
            params['email'],
            params['code'],
        )
        # 校验email code
        status = verifyCaptcha(email, code)
        if status == 1:
            return make_error_response(msg='验证码过期'), 400
        elif status == 2:
            return make_error_response(msg='验证码不正确'), 400

        # 验证账号密码
        try:
            stmt_select_username = select(User).where(User.username == username)
            with Session(engine) as session:
                rows = session.execute(stmt_select_username)
                if len(list(rows)) > 0:
                    return make_error_response(msg='用户名已存在'), 400
            
            stmt_select_email = select(User).where(User.email == email)
            with Session(engine) as session:
                rows = session.execute(stmt_select_email)
                if len(list(rows)) > 0:
                    return make_error_response(msg='邮箱已存在'), 400

            with engine.connect() as conn:
                conn.execute(
                    insert(User),
                    [{'username': username, 'password': password, 'email': email}],
                )
                conn.commit()

            return make_success_response(msg='注册成功')
        except Exception as e:
            print(e)
            return make_error_response(msg='注册失败'), 500


class SendMail(Resource):
    def post(self):
        email = request.form['email']
        
        return sendCaptcha(email)


user_blueprint = Blueprint('user', __name__, url_prefix='/user')
user_api = Api(user_blueprint)
user_api.add_resource(UsernameBasedLogin, '/username/login')
user_api.add_resource(EmailBasedLogin, '/email/login')
user_api.add_resource(Regist, '/regist')
user_api.add_resource(SendMail, '/mail')