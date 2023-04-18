import hashlib
import uuid
from flask_restful import Resource, fields, reqparse, marshal
from config import get_dyn_data, mark_dyn_data
from resources.readability_indicator.util import Readability
from utils.jwt import check_premission
from utils.json_response import make_success_response

parser = reqparse.RequestParser()
parser.add_argument('lg_text', required=True, location='form')
parser.add_argument('lg_type', required=True, location='form')


def generateHash(text: str):
    hash_model = hashlib.md5()
    hash_model.update(text.encode('utf-8'))
    return hash_model.hexdigest()


def getHandler(parser=parser, id=None) -> Readability:
    args = parser.parse_args()
    lg_text = args['lg_text']
    lg_type = args['lg_type']
    hash_value = generateHash(lg_text)
    handler = get_dyn_data(hash_value)
    if handler is None:
        handler = Readability(lg_text, lg_type)
        mark_dyn_data(hash_value, handler)

    return handler


def handleIndicatorReturn(**kargs):
    return make_success_response(data={kargs['type']: kargs['value']})


class ARI(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getARI()

        return handleIndicatorReturn(value=ans, type='ARI')


class ARIGradeLevels(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getARIGradeLevels()

        return handleIndicatorReturn(value=ans, type='ARIGradeLevel')


class RIX(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getRIX()

        return handleIndicatorReturn(value=ans, type='ARIGradeLevel')


class FlsechKincaidGrade(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getFlsechKincaidGrade()

        return handleIndicatorReturn(value=ans, type='ARIGradeLevel')


class GunningFog(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getGunningFog()

        return handleIndicatorReturn(value=ans, type='ARIGradeLevel')


class Smog(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getSmog()

        return handleIndicatorReturn(value=ans, type='ARIGradeLevel')


class ColemanLiauIndex(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getColemanLiauIndex()

        return handleIndicatorReturn(value=ans, type='ARIGradeLevel')


class DaleChallIndex(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getDaleChallIndex()

        return handleIndicatorReturn(value=ans, type='ARIGradeLevel')


class LWIndex(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getLWIndex()

        return handleIndicatorReturn(value=ans, type='LWIndex')

class FleschReading(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ans = handler.getFleschReading()

        return handleIndicatorReturn(value=ans, type='FleschReading')



class AllReadability(Resource):
    @check_premission
    def post(self, info):
        handler = getHandler(parser=parser, id=info['user_id'])
        ARI_Value = handler.getARI()
        ARIGradeLevels_Value = handler.getARIGradeLevels()
        RIX_Value = handler.getRIX()
        FleschReading_Value = handler.getFleschReading()
        FlsechKincaidGrade_Value = handler.getFlsechKincaidGrade()
        GunningFog_Value = handler.getGunningFog()
        Smog_Value = handler.getSmog()
        ColemanLiauIndex_Value = handler.getColemanLiauIndex()
        DaleChallIndex_Value = handler.getDaleChallIndex()
        LWIndex_Value = handler.getLWIndex()

        data = {
                "ARI": ARI_Value,
                "ARIGradeLevels": ARIGradeLevels_Value,
                "RIX": RIX_Value,
                "FleschReading": FleschReading_Value,
                "FlsechKincaidGrade": FlsechKincaidGrade_Value,
                "GunningFog": GunningFog_Value,
                "Smog": Smog_Value,
                "ColemanLiauIndex": ColemanLiauIndex_Value,
                "DaleChallIndex": DaleChallIndex_Value,
                "LWIndex": LWIndex_Value,
            }
        hash_id = uuid.uuid4().__repr__()[6:-3]
        mark_dyn_data(hash_id, data)
        data['hash_value'] = hash_id

        return make_success_response(data=data)
