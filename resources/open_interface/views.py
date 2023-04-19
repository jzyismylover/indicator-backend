# 开发 API 接口
import functools
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, update
from flask_restful import Resource, reqparse, request
from utils.jwt import check_premission, verify_token
from utils.jwt.generateHash import generate_hash_password
from utils.jwt.generateAppid import generate_app_id
from utils.json_response import make_error_response, make_success_response
from config.db import engine
from config.db.user import User
from resources.Language import LanguageRec, LAN_MAPPER
from resources.common_indicator.util import CommonIndicatorHandler
from resources.readability_indicator.util import Readability
from resources.constant import (
    COMMON_INDICATOR_HANDLER_MAPPING,
    READABILITY_INDICATOR_HANDLER_MAPPING,
    CUMYLATIVE_INDICATORS,
)

language_ins = LanguageRec()


def check_app_id(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # if token exists, do not need to verify the appid
        headers = request.headers
        if 'HTTP_AUTHORIZATION' in headers.environ:
            token = headers.environ['HTTP_AUTHORIZATION'][7:]
            auth = verify_token(token)
            if auth['status'] == 200:
                return fn(*args, **kwargs)
                
        if 'appid' not in request.form:
            return make_error_response(msg='missing appid'), 400
        appid = request.form['appid']
        with Session(engine) as session:
            stmt = select(User).where(User.appid == appid)
            results = session.execute(stmt)
            if len(list(results)) <= 0:
                return make_error_response(msg='invalid appid'), 400

        return fn(*args, **kwargs)

    return wrapper


class GenerateAppId(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('password', required=True, location='form')

    @check_premission
    def post(self, info):
        params = self.parser.parse_args()
        password = generate_hash_password(params['password'])
        with Session(engine) as session:
            stmt = select(User).where(
                and_(User.password == password, User.id == info['user_id'])
            )
            row = session.scalars(stmt).first()
            if row is None:
                return make_error_response(msg='用户密码错误'), 400

        if row.appid is not None:
            return make_success_response(data={'appid': row.appid})
        appid = generate_app_id(row.username, row.email, row.password)
        # store appid
        with engine.begin() as conn:
            stmt = update(User).where(User.id == info['user_id']).values(appid=appid)
            conn.execute(stmt)

        return make_success_response(data={'appid': appid})


class GetAppid(Resource):
    @check_premission
    def get(self, info):
        with Session(engine) as session:
            stmt = select(User).where(User.id == info['user_id'])
            row = session.scalars(stmt).first()

        return make_success_response(data={'appid': row.appid})


class CommonIndicatorsOpenApi(Resource):
    def __init__(self) -> None:
        self.files = request.files.getlist('files')
        params = request.form
        if 'indicators' not in params:
            self.indicators = COMMON_INDICATOR_HANDLER_MAPPING.keys()
        else:
            self.indicators = params['indicators'].split(',')
        if 'requireSplit' not in params:  # 默认执行分句分词
            self.requireSplit = False
        else:
            self.requireSplit = self.get_bool_from_form(params['requireSplit'])
        if 'cumulatives' not in params:
            self.cumulatives = self.indicators
        else:
            self.cumulatives = params['cumulatives'].split(',')

    def get_bool_from_form(self, val):
        if val == 'false':
            return False
        else:
            return True

    def culmulateWords(
        self, model: CommonIndicatorHandler, cumulative_model: CommonIndicatorHandler
    ):
        cumulative_model.words.extend(model.words)

    def culmulateFrequency(self, cumulative_model: CommonIndicatorHandler):
        ans = cumulative_model.handler.get_word_frequency(cumulative_model.words)
        cumulative_model.frequency = ans['frequency']
        cumulative_model.frequency_words = ans['frequency_words']
        cumulative_model.hapax = ans['hapax']

    def culmulateTags(
        self, model: CommonIndicatorHandler, cumulative_model: CommonIndicatorHandler
    ):
        cumulative_model.tags.extend(model.tags)

    def calculate(self):
        results = []
        base_lg_type = None
        models = []

        for file in self.files:
            lg_type, content = language_ins.parse_file(file)
            base_lg_type = lg_type
            model = CommonIndicatorHandler(content, lg_type, self.requireSplit)
            models.append(model)
            ans = dict()
            ans['filename'] = file.filename
            for _ in self.indicators:
                if _ not in COMMON_INDICATOR_HANDLER_MAPPING:
                    continue
                func = getattr(model, COMMON_INDICATOR_HANDLER_MAPPING[_], None)
                # 非增量指标累计
                score = func()
                ans[_] = score

            results.append(ans)

        # 增量指标
        culmulative_dic = dict()
        if len(self.cumulatives) > 0:
            model = CommonIndicatorHandler('', base_lg_type)
            model.words.pop()
            for mdl in models:
                self.culmulateWords(mdl, model)
                self.culmulateTags(mdl, model)

            self.culmulateFrequency(model)

            for _ in self.cumulatives:
                if _ in CUMYLATIVE_INDICATORS:
                    culmulative_dic[_] = getattr(
                        model, COMMON_INDICATOR_HANDLER_MAPPING[_], None
                    )()
        
        return {
            'results': results,
            'culmulative_dic': culmulative_dic
        }

    @check_app_id
    def post(self):
        ans = self.calculate()
        results = ans['results']
        culmulative_dic = ans['culmulative_dic']
        return make_success_response(
            data={
                'directory_indicators': results,
                'cumulative_indicators': culmulative_dic,
            }
        )


class LanguageRecognizeOpenApi(Resource):
    @check_app_id
    def post(self):
        params = request.form
        if 'text' not in params:
            return make_error_response(msg='missing required params text'), 400

        text = params['text']
        lg_type = language_ins.get_text_lg_type(text)
        if lg_type not in LAN_MAPPER:
            return make_error_response(msg='不支持该类语种识别'), 500

        return make_success_response(
            data={'lg_type': lg_type, 'lg_name': LAN_MAPPER[lg_type], 'lg_text': text}
        )


class TextAnalyseinWordSplitOpenApi(Resource):
    @check_app_id
    def post(self):
        if 'text' in request.form:
            text = request.form['text']
            lg_type = language_ins.get_text_lg_type(text)
            model = CommonIndicatorHandler(text, lg_type)
            words = model.words
            return make_success_response(data=words)
        elif len(request.files.getlist('files')) > 0:
            words = []
            for file in request.files.getlist('files'):
                lg_type, content = language_ins.parse_file(file)
                model = CommonIndicatorHandler(content, lg_type)
                words.extend(model.words)
            return make_success_response(data=words)
        else:
            return make_success_response()


class TextAnalyseinTaggingOpenApi(Resource):
    @check_app_id
    def post(self):
        if 'text' in request.form:
            text = request.form['text']
            lg_type = language_ins.get_text_lg_type(text)
            model = CommonIndicatorHandler(text, lg_type)
            tags = model.handleSpeechTagging()
            return make_success_response(data=tags)
        elif len(request.files.getlist('files')) > 0:
            tags = []
            for file in request.files.getlist('files'):
                lg_type, content = language_ins.parse_file(file)
                model = CommonIndicatorHandler(content, lg_type)
                tags.extend(model.handleSpeechTagging())
            return make_success_response(data=tags)
        else:
            return make_success_response()


class ReadabilityIndicatorOpenApi(Resource):
    @check_app_id
    def post(self):
        files = request.files.getlist('files')
        params = request.form
        if len(files) <= 0:
            return make_error_response(msg='missing required param files')
        if 'indicators' not in params:
            indicators = READABILITY_INDICATOR_HANDLER_MAPPING.keys()
        else:
            indicators = params['indicators'].split(',')

        results = []
        for file in files:
            lg_type, content = language_ins.parse_file(file)
            model = Readability(content, lg_type)
            ans = dict()
            ans['filename'] = file.filename
            for _ in indicators:
                if _ not in READABILITY_INDICATOR_HANDLER_MAPPING:
                    continue
                func = getattr(model, READABILITY_INDICATOR_HANDLER_MAPPING[_], None)
                ans[_] = func()

            results.append(ans)

        return make_success_response(data=results)