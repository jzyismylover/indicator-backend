from flask_restful import Resource, fields, reqparse, marshal_with
import re

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
    'password', type=verify_passwd, required=True, location='form', help='password: invalid: {error_msg}'
)
user_field = {'username': fields.String, 'password': fields.String, 'msg': fields.String(attribute='message')}


class Login(Resource):
    @marshal_with(fields=user_field, envelope='data')
    def post(self):
        params = login_parser.parse_args()
        username, password = params['username'], params['password']
        return {'username': username, 'password': password}
        

regist_parser = login_parser.copy()
regist_parser.add_argument('confirm_password', type=verify_passwd, location='form', required=True)


class Regist(Resource):
    @marshal_with(fields=user_field, envelope='data')
    def post(self):
        params = regist_parser.parse_args()
        username, password, confirm_passwd = (
            params['username'],
            params['password'],
            params['confirm_password'],
        )
        if password != confirm_passwd:
            return {
              'message': '密码不一致'
            }, 400
        else:
            return {'username': username, 'password': password}
