import re
from flask_restful import Resource, fields, reqparse, marshal_with
from utils.jwt import create_token
from config import mark_dyn_data, get_dyn_data

def verify_passwd(value, name):
    res = re.search(
        '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()_\-+])[A-Za-z\d~!@#$%^&*()_\-+]{8,16}$',
        value,
    )
    if res is None:
        raise ValueError('密码需满足至少8位且包含数字大小写字母以及特殊字符')
    else:
        return value


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True, location='form')
login_parser.add_argument(
    'password', type=verify_passwd, required=True, location='form', help='{error_msg}'
)
user_field = {'msg': fields.String(attribute='message')}


class Login(Resource):
    @marshal_with(fields=user_field, envelope='data')
    def post(self):
        params = login_parser.parse_args()
        username, password = params['username'], params['password']
        token = create_token(username, password)
        return {
            'message': '登录成功' 
        }, 200
        

regist_parser = login_parser.copy()
regist_parser.add_argument('confirm_password', type=verify_passwd, location='form', required=True)
class Regist(Resource):
    @marshal_with(fields=user_field, envelope='data')
    def post(self):
        params = regist_parser.parse_args()
        username, password, code = (
            params['username'],
            params['password'],
        )
        code = get_dyn_data(username, code)