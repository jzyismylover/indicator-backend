# 获取个人信息接口
from flask import Blueprint
from flask_restful import Resource, reqparse, Api
from config.db import engine
from config.db.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select, update, or_, and_
from utils.jwt import check_premission
from utils.json_response import make_success_response, make_error_response
from utils.jwt.generateHash import generate_hash_password


class GetUserInfo(Resource):
    @check_premission
    def get(self, info):
        user_id = info['user_id']
        with Session(engine) as session:
            rows = session.scalars(select(User).where(User.id == user_id)).first()

        return make_success_response({'username': rows.username, 'email': rows.email})


class UpdateUserInfo(Resource):
    @check_premission
    def put(self, info):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='form')
        parser.add_argument('email', location='form')
        param = parser.parse_args()
        username = param['username']
        email = param['email']
        # username / email must not in databases
        with Session(engine) as session:
            rows = session.scalars(
                select(User).where(and_(or_(User.username == username, User.email == email), User.id != info['user_id']))
            ).first()
            if rows is not None:
                return make_error_response(msg='用户/邮箱已存在'), 400
        try:
            with engine.begin() as conn:
                stmt = (
                    update(User)
                    .where(User.id == info['user_id'])
                    .values(username=username, email=email)
                )
                conn.execute(stmt)
        except Exception as e:
            print(e)
            return make_error_response(msg='error'), 500

        return make_success_response(msg='success')


class UpdateUserPassword(Resource):
    @check_premission
    def put(self, info):
        # 更新账户密码
        parser = reqparse.RequestParser()
        parser.add_argument('prev_password', location='form')
        parser.add_argument('curr_password', location='form')
        param = parser.parse_args()
        prev_password = param['prev_password']
        curr_password = param['curr_password']
        try:
            with Session(engine) as session:
                rows = session.scalars(
                    select(User).where(User.id == info['user_id'])
                ).first()
                if generate_hash_password(prev_password) != rows.password:
                    return make_error_response(msg='当前用户密码不正确'), 400

            with engine.begin() as conn:
                stmt = (
                    update(User)
                    .where(User.id == info['user_id'])
                    .values(password=generate_hash_password(curr_password))
                )
                conn.execute(stmt)
        except:
            return make_error_response(msg='修改失败'), 500

        return make_success_response(msg='密码修改成功')


info_blueprint = Blueprint('info', __name__)
info_api = Api(info_blueprint)
info_api.add_resource(GetUserInfo, '/getUserInfo')
info_api.add_resource(UpdateUserInfo, '/updateUserInfo')
info_api.add_resource(UpdateUserPassword, '/updateUserPassword')
