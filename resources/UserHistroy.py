from flask_restful import Api, Resource, reqparse, request
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from utils.jwt import check_premission
from utils.json_response import make_success_response, make_error_response
from config.db.history import History
from config.db import engine


def get_history_rows(user_id):
    with Session(engine) as session:
        stmt = select(History).where(History.user_id == user_id)
        rows = session.execute(stmt).all()
        rows = list(rows)[-10:]
        histories = []
        # 实际每个item都是(..., )元组
        for item in rows:
            item = item[0]
            histories.append(
                {
                    'id': item.id,
                    'lg_text': item.content,
                    'lg_type': item.type,
                }
            )
    return histories


def deleteHistory(id, _user_id):
    with Session(engine) as session:
        stmt = select(History).where(History.id == id)
        rows = session.execute(stmt)
        rows = list(rows)
        row = rows[0][0]
        user_id = row.user_id

        if user_id != _user_id:
            return
        else:
          with engine.begin() as conn:
              stmt = delete(History).where(History.id == id)
              conn.execute(stmt)


class UserHistory(Resource):
    @check_premission
    def get(self, info):
        histories = get_history_rows(info['user_id'])
        return make_success_response(data=histories)

    @check_premission
    def delete(self, info):
        parser = reqparse.RequestParser()
        parser.add_argument('history_id', required=True, location='form')
        params = parser.parse_args()

        history_id = [int(id) for id in params['history_id'].split(',')]
        for item in history_id:
          deleteHistory(item, info['user_id'])

        histories = get_history_rows(info['user_id'])

        return make_success_response(data=histories, msg='删除成功')