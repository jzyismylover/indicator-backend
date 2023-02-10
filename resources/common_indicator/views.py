import math
import hashlib
from flask_restful import Resource, reqparse, fields, marshal
from utils import EN_Utils, ZH_Utils, Base_Utils
from config import get_dyn_data, mark_dyn_data
from resources.common_indicator.util import *

parser = reqparse.RequestParser()
parser.add_argument('lg_type', type=str, required=True, location='form')
parser.add_argument('lg_text', type=str, required=True, location='form')

OUTPUT_FIELDS = {
    'type': fields.String,
    'value': fields.Float,
}

LANGUAGE_HANDLER_MAPPER = {'en': EN_Utils, 'zh': ZH_Utils}


def generateHash(text: str):
    hash_model = hashlib.md5()
    hash_model.update(text.encode('utf-8'))
    return hash_model.hexdigest()


def getParams(parser) -> Base_Utils:
    params = parser.parse_args()
    lg_type = params['lg_type']
    lg_text = params['lg_text']
    hash_value = generateHash(lg_type + lg_text)
    handler = getLanguageHandler(lg_type, lg_text, hash_value=hash_value)
    return handler


def getLanguageHandler(lg_type, lg_text, *, hash_value=''):
    handler = get_dyn_data(hash_value)
    if handler == None:
        handler = LANGUAGE_HANDLER_MAPPER[lg_type]
        mark_dyn_data(hash_value, handler)
    handler = LANGUAGE_HANDLER_MAPPER[lg_type]
    return handler(lg_text)


def handleIndicatorReturn(*, value, type, fields=OUTPUT_FIELDS):
    if fields == OUTPUT_FIELDS:
        data = {'value': value, 'type': type}
    else:
        data = {x: value[x] for x in value.keys()}
    return marshal(data=data, fields=fields, envelope='data')


"""
具体指标计算视图
"""


class TTRValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        ans = getTTRValue(frequency=handler.frequency, words=handler.words)

        return handleIndicatorReturn(value=ans, type='TTR')


class HPoint(Resource):
    def post(self):
        handler = getParams(parser=parser)

        if handler.h_value == 0:
            handler.get_h_value()

        return handleIndicatorReturn(value=handler.h_value, type='Hpoint')


class EntropyValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        H = getEntroyValue(frequency=handler.frequency, words=handler.words)

        return handleIndicatorReturn(value=H, type='Entropy')


"""
暂时省略 Average Tokens Length & Token Length Frequency Specturm
"""


class R1Value(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if handler.h_value == 0:
            handler.get_h_value()

        R1 = getR1Value(
            frequency=handler.frequency, words=handler.words, h_value=handler.h_value
        )

        return handleIndicatorReturn(value=R1, type='R1')


class RRValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        RR = getRRValue(words=handler.words, frequency=handler.frequency)
        return handleIndicatorReturn(value=RR, type='RR')


class RRmcValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        RRmc = getRRmcValue(frequency=handler.frequency, words=handler.words)

        return handleIndicatorReturn(value=RRmc, type='RRmc')


class TCValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if len(handler.real_words) == 0:
            handler.get_real_words()
        if handler.h_value == 0:
            handler.get_h_value()

        Tr = getTCValue(
            frequency=handler.frequency,
            h_value=handler.h_value,
            frequency_words=handler.frequency_words,
            real_words=handler.real_words,
        )

        return handleIndicatorReturn(value=Tr, type='TC')


class SecondaryTCValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if len(handler.real_words) == 0:
            handler.get_real_words()
        if handler.h_value == 0:
            handler.get_h_value()

        Tr = getSecondTCValue(
            frequency=handler.frequency,
            h_value=handler.h_value,
            frequency_words=handler.frequency_words,
            real_words=handler.real_words,
        )

        return handleIndicatorReturn(value=Tr, type='Secondary')


class ActivityValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        verb_words = handler.get_verb_words()
        adjective_words = handler.get_adjective_words()
        activity = getAcitvityValue(
            verb_words=verb_words, adjective_words=adjective_words
        )

        return handleIndicatorReturn(value=activity, type='Activity')


class DescriptivityValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        verb_words = handler.get_verb_words()
        adjective_words = handler.get_adjective_words()
        descriptivity = getDescriptivityValue(
            verb_words=verb_words, adjective_words=adjective_words
        )

        return handleIndicatorReturn(value=descriptivity, type='Descriptivity')


class LValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        L = getLValue(frequency=handler.frequency)

        return handleIndicatorReturn(value=L, type='L')


class CurveLengthValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if handler.h_value == 0:
            handler.get_h_value()

        f = handler.frequency
        h = handler.h_value
        R = getCurveLengthValue(frequency=f, h_value=h)

        return handleIndicatorReturn(value=R, type='Curve Length R Index')


class LambdaValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        lambda_v = getLambdaValue(frequency=handler.frequency, words=handler.words)

        return handleIndicatorReturn(value=lambda_v, type='lambda')


class AdjustedModuleValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if handler.h_value == 0:
            handler.get_h_value()

        h = handler.h_value
        f = handler.frequency
        V = len(handler.frequency)
        N = len(handler.words)
        f1 = f[0]
        M = math.sqrt((f1 / h) ** 2 + (V / h) ** 2)

        A = M / math.log10(N)

        return handleIndicatorReturn(value=A, type='Adjusted Modules')


class GiniValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        G = getGiniValue(frequency=handler.frequency, words=handler.words)

        return handleIndicatorReturn(value=G, type='G')


class R4Value(Resource):
    def post(self):
        handler = getParams(parser=parser)

        R4 = getR4Value(frequency=handler.frequency, words=handler.words)

        return handleIndicatorReturn(value=R4, type='R4')


class HapaxValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        rate = getHapaxValue(words=handler.words, hapax=handler.hapax)

        return handleIndicatorReturn(value=rate, type='Hapax Percentage')


class WriterView(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if handler.h_value == 0:
            handler.get_h_value()

        cosa = getWriterView(frequency=handler.frequency, h_value=handler.h_value)

        return handleIndicatorReturn(value=cosa, type='Writer\'s View')


class VerbDistance(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if len(handler.tags) == 0:
            handler.get_word_character()

        tags = handler.tags
        verb_V = getVerbDistance(tags=handler.tags, is_verb_word=handler.is_verb_word)

        return handleIndicatorReturn(value=verb_V, type='Verb Distances')


class ZipfTest(Resource):
    def post(self):
        handler = getParams(parser=parser)

        zipf = getZipf(
            frequency=handler.frequency, frequency_words=handler.frequency_words
        )

        current_fields = {str(x): fields.Float for x in zipf.keys()}
        return handleIndicatorReturn(
            value=zipf, fields=current_fields, type='Zipf Test'
        )


class ALLCommonIndicator(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if len(handler.real_words) == 0:
            handler.get_real_words()
        if handler.h_value == 0:
            handler.get_h_value()

        f = handler.frequency
        w = handler.words
        h = handler.h_value
        verb_words = handler.get_verb_words()
        adjective_words = handler.get_adjective_words()

        RR = getRRValue(frequency=f, words=w)
        Activity = getAcitvityValue(
            verb_words=verb_words, adjective_words=adjective_words
        )
        L = getLValue(frequency=f)
        G = getGiniValue(frequency=f, words=w)

        return {
            'data': {
                'TTR': getTTRValue(frequency=f, words=w),
                'HPoint': h,
                'Entropy': getEntroyValue(frequency=f, words=w),
                'R1': getR1Value(frequency=f, words=w, h_value=h),
                'RR': getRRValue(frequency=f, words=w),
                'RRmc': getRRmcValue(frequency=f, words=w, RR=RR),
                'TC': getTCValue(
                    frequency=f, 
                    real_words=handler.real_words,
                    h_value=h,
                    frequency_words=handler.frequency_words
                ),
                'SecondTc': getSecondTCValue(
                    frequency=f, 
                    real_words=handler.real_words,
                    h_value=h,
                    frequency_words=handler.frequency_words
                ),
                'Activity': Activity,
                'Descriptivity': 1 - Activity,
                'L': getLValue(frequency=f),
                'Curver Length R Index': getCurveLengthValue(frequency=f, h_value=h),
                'Lambda': getLambdaValue(frequency=f, words=w, L=L),
                'G': G,
                'R4': 1 - G,
                'Hapax Percentage': getHapaxValue(words=w, hapax=handler.hapax),
                'Writer\'s View': getWriterView(frequency=f, h_value=h),
                'Verb Distances': getVerbDistance(
                    tags=handler.tags, is_verb_word=handler.is_verb_word
                ),
                'Zipf Test': getZipf(
                    frequency=f, frequency_words=handler.frequency_words
                ),
            }
        }
