import math
import hashlib
from flask_restful import Resource, reqparse, fields, marshal
from config import get_dyn_data, mark_dyn_data
from resources.common_indicator.util import *

parser = reqparse.RequestParser()
parser.add_argument('lg_type', type=str, required=True, location='form')
parser.add_argument('lg_text', type=str, required=True, location='form')


def generateHash(text: str):
    hash_model = hashlib.md5()
    hash_model.update(text.encode('utf-8'))
    return hash_model.hexdigest()


def getParams(parser) -> CommonIndicatorHandler:
    params = parser.parse_args()
    lg_type = params['lg_type']
    lg_text = params['lg_text']
    hash_value = generateHash(lg_type + lg_text)
    handler = getLanguageHandler(lg_text, lg_type, hash_value=hash_value)
    return handler


def getLanguageHandler(lg_text, lg_type, *, hash_value=''):
    try:
        handler = get_dyn_data(hash_value)
        if handler == None:
            handler = CommonIndicatorHandler(text=lg_text, lg_type=lg_type)
            mark_dyn_data(hash_value, handler)
    except Exception as e:
        print(e)
        pass
    return handler


def handleIndicatorReturn(**kargs):
    return {
        'data': {
            kargs['type']: kargs['value']
        }
    }


"""
具体指标计算视图
"""


class TTRValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        ans = handler.getTTRValue()

        return handleIndicatorReturn(value=ans, type='TTR')


class HPoint(Resource):
    def post(self):
        handler = getParams(parser=parser)
        h_point = handler.getHPoint()

        return handleIndicatorReturn(value=h_point, type='Hpoint')


class EntropyValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        H = handler.getEntroyValue()

        return handleIndicatorReturn(value=H, type='Entropy')


"""
暂时省略 Average Tokens Length & Token Length Frequency Specturm
"""


class R1Value(Resource):
    def post(self):
        handler = getParams(parser=parser)
        R1 = handler.getR1Value()

        return handleIndicatorReturn(value=R1, type='R1')


class RRValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        RR = handler.getRRValue()

        return handleIndicatorReturn(value=RR, type='RR')


class RRmcValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        RRmc = handler.getRRmcValue()

        return handleIndicatorReturn(value=RRmc, type='RRmc')


class TCValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        Tr = handler.getTCValue()

        return handleIndicatorReturn(value=Tr, type='TC')


class SecondaryTCValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        Tr = handler.getSecondTCValue()

        return handleIndicatorReturn(value=Tr, type='Secondary')


class ActivityValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        activity = handler.getAcitvityValue( )

        return handleIndicatorReturn(value=activity, type='Activity')


class DescriptivityValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        descriptivity = handler.getDescriptivityValue()

        return handleIndicatorReturn(value=descriptivity, type='Descriptivity')


class LValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        L = handler.getLValue()

        return handleIndicatorReturn(value=L, type='L')


class CurveLengthValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        R = handler.getCurveLengthValue()

        return handleIndicatorReturn(value=R, type='Curve Length R Index')


class LambdaValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        lambda_v = handler.getLambdaValue()

        return handleIndicatorReturn(value=lambda_v, type='lambda')


class AdjustedModuleValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        A = handler.getAdjustModuleValue()

        return handleIndicatorReturn(value=A, type='Adjusted Modules')


class GiniValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        G = handler.getGiniValue()

        return handleIndicatorReturn(value=G, type='G')


class R4Value(Resource):
    def post(self):
        handler = getParams(parser=parser)
        R4 = handler.getR4Value()

        return handleIndicatorReturn(value=R4, type='R4')


class HapaxValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        rate = handler.getHapaxValue()

        return handleIndicatorReturn(value=rate, type='Hapax Percentage')


class WriterView(Resource):
    def post(self):
        handler = getParams(parser=parser)
        cosa = handler.getWriterView()

        return handleIndicatorReturn(value=cosa, type='Writer\'s View')


class VerbDistance(Resource):
    def post(self):
        handler = getParams(parser=parser)
        verb_V = handler.getVerbDistance()

        return handleIndicatorReturn(value=verb_V, type='Verb Distances')


class ZipfTest(Resource):
    def post(self):
        handler = getParams(parser=parser)
        zipf = handler.getZipf()
        current_fields = {str(x): fields.Float for x in zipf.keys()}

        return handleIndicatorReturn(
            value=zipf, fields=current_fields, type='Zipf Test'
        )


class ALLCommonIndicator(Resource):
    def post(self):
        handler = getParams(parser=parser)
        h = handler.getHPoint()
        Activity = handler.getAcitvityValue()
        G = handler.getGiniValue()

        return {
            'data': {
                'TTR': handler.getTTRValue(),
                'HPoint': h,
                'Entropy': handler.getEntroyValue(),
                'R1': handler.getR1Value(),
                'RR': handler.getRRValue(),
                'RRmc': handler.getRRmcValue(),
                'TC': handler.getTCValue(),
                'SecondTc': handler.getSecondTCValue(),
                'Activity': Activity,
                'Descriptivity': 1 - Activity,
                'L': handler.getLValue(),
                'Curver Length R Index': handler.getCurveLengthValue(),
                'Lambda': handler.getLambdaValue(),
                'G': G,
                'R4': 1 - G,
                'Hapax Percentage': handler.getHapaxValue(),
                'Writer\'s View': handler.getWriterView(),
                'Verb Distances': handler.getVerbDistance(),
                'Zipf Test': handler.getZipf(),
            }
        }
