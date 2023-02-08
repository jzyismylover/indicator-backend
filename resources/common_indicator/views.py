import pickle
import math
import hashlib
from flask_restful import Resource, reqparse, fields, marshal
from utils import EN_Utils, ZH_Utils, Base_Utils
from config import get_dyn_data, mark_dyn_data

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


def getRRValue(*, words, frequency):
    N = len(words)
    RR = 0
    for num in frequency:
        RR += (num / N) ** 2

    return RR


def getLValue(*, frequency):
    L = 0
    for i in range(0, len(frequency) - 1):
        distance = (frequency[i] - frequency[i + 1]) ** 2
        L += math.sqrt(distance + 1)

    return L


def getGiniValue(*, N, V, frequency: list):
    c1 = 0
    for i, num in enumerate(frequency):
        c1 += (i + 1) * num
    c1 = 2 * c1 / N
    G = (V + 1 - c1) / V

    return G


"""
具体指标计算视图
"""


class TTRValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        print(handler.frequency, handler.words)
        ans = len(handler.frequency) / len(handler.words)

        return handleIndicatorReturn(value='{:.2f}'.format(ans), type='TTR 指标')


class HPoint(Resource):
    def post(self):
        handler = getParams(parser=parser)

        if handler.h_value == 0:
            handler.get_h_value()

        return handleIndicatorReturn(value=handler.h_value, type='Hpoint 指标')


class EntropyValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        N = len(handler.words)
        H = 0

        for num in handler.frequency:
            rate = num / N
            H += rate * math.log2(rate)

        return handleIndicatorReturn(value=H, type='Entropy 熵')


"""
暂时省略 Average Tokens Length & Token Length Frequency Specturm
"""


class R1Value(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if handler.h_value == 0:
            handler.get_h_value()

        N = len(handler.words)
        h = handler.h_value
        t = 0
        for i, num in enumerate(handler.frequency):
            if (i + 1) > h:
                break
            t += num

        Fh = t / N
        h = handler.h_value
        Fh_ = Fh - (h**2) / (2 * N)
        R1 = 1 - Fh_

        return handleIndicatorReturn(value=R1, type='词汇丰富度')


class RRValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        RR = getRRValue(words=handler.words, frequency=handler.frequency)
        return handleIndicatorReturn(value=RR, type='重复率')


class RRmcValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        RR = getRRValue(words=handler.words, frequency=handler.frequency)
        V = len(handler.frequency)
        RRmc = (1 - math.sqrt(RR)) / (1 - 1 / math.sqrt(V))

        return handleIndicatorReturn(value=RRmc, type='相对重复率')


class TCValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if len(handler.real_words) == 0:
            handler.get_real_words()
        if handler.h_value == 0:
            handler.get_h_value()

        Tr = 0
        h = handler.h_value
        f = handler.frequency
        for i, fr in enumerate(f):
            if i + 1 > h:
                break
            word = handler.frequency_words[i]
            if handler.real_words.count(word) != 0:
                Tr += ((h - (i + 1)) * fr) / (h * (h - 1) * f[0])
        Tr = Tr * 2

        return handleIndicatorReturn(value=Tr, type='主题集中度')


class SecondaryTCValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if len(handler.real_words) == 0:
            handler.get_real_words()
        if handler.h_value == 0:
            handler.get_h_value()

        Tr = 0
        h = handler.h_value
        f = handler.frequency
        for i in range(math.ceil(h), math.floor(2 * h) + 1):
            word = handler.frequency_words[i - 1]
            if handler.real_words.count(word) != 0:
                fr = f[i - 1]
                Tr += ((h - i) * fr) / (h * (h - 1) * f[0])

        return handleIndicatorReturn(value=Tr, type='次级主题集中度')


class ActivityValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        verb_words = len(handler.get_verb_words())
        adjective_words = len(handler.get_adjective_words())
        activity = verb_words / (verb_words + adjective_words)

        return handleIndicatorReturn(value=activity, type='活动度')


class DescriptivityValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        verb_words = len(handler.get_verb_words())
        adjective_words = len(handler.get_adjective_words())

        descriptivity = adjective_words / (verb_words + adjective_words)

        return handleIndicatorReturn(value=descriptivity, type='描写度')


class LValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        L = getLValue(frequency=handler.frequency)

        return handleIndicatorReturn(value=L, type='秩序分布欧氏距离')


class CurveLengthValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if handler.h_value == 0:
            handler.get_h_value()

        f = handler.frequency
        h = handler.h_value
        LR = 0
        L = 0
        for i in range(0, len(f) - 1):
            distance = (f[i] - f[i + 1]) ** 2
            if i + 1 < h:
                LR += math.sqrt(distance + 1)
            L += math.sqrt(distance + 1)

        R = 1 - LR / L

        return handleIndicatorReturn(value=R, type='秩序分布 R 指数')


class LambdaValue(Resource):
    def post(self):
        handler = getParams(parser=parser)
        L = getLValue(frequency=handler.frequency)
        N = len(handler.words)

        Lambda_v = (L * math.log10(N)) / N

        return handleIndicatorReturn(value=Lambda_v, type='lambda 值')


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

        return handleIndicatorReturn(value=A, type='校正模数')


class GiniValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        V = len(handler.frequency)
        N = len(handler.words)
        f = handler.frequency
        G = getGiniValue(V=V, N=N, frequency=f)

        return handleIndicatorReturn(value=G, type='基尼系数')


class R4Value(Resource):
    def post(self):
        handler = getParams(parser=parser)

        V = len(handler.frequency)
        N = len(handler.words)
        f = handler.frequency
        G = getGiniValue(V=V, N=N, frequency=f)
        R4 = 1 - G

        return handleIndicatorReturn(value=R4, type='R4')


class HapaxValue(Resource):
    def post(self):
        handler = getParams(parser=parser)

        N = len(handler.words)
        hpaxRate = len(handler.hapax) / N

        return handleIndicatorReturn(value=hpaxRate, type='单现词占比')


class WriterView(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if handler.h_value == 0:
            handler.get_h_value()

        h = handler.h_value
        f = handler.frequency
        V = len(handler.frequency)
        f1 = f[0]

        r1 = h - 1
        r2 = f1 - h
        r3 = h - 1
        r4 = V - h

        t1 = -(r1 * r2 + r3 * r4)
        t2 = math.sqrt(r1**2 + r2**2)
        t3 = math.sqrt(r3**2 + r4**2)

        cosa = t1 / (t2 * t3)

        return handleIndicatorReturn(value=cosa, type='作者视野')


class VerbDistance(Resource):
    def post(self):
        handler = getParams(parser=parser)
        if len(handler.tags) == 0:
            handler.get_word_character()

        tags = handler.tags
        verb_V = 0
        verb_idx_list = []
        for i, tag in enumerate(tags):
            if handler.is_verb_word(tag):
                verb_idx_list.append(i)

        for i in range(0, len(verb_idx_list) - 1):
            verb_V += verb_idx_list[i + 1] - verb_idx_list[i]
        verb_V = verb_V / (len(verb_idx_list) - 1)

        return handleIndicatorReturn(value=verb_V, type='动词间距')


class ZipfTest(Resource):
    def post(self):
        handler = getParams(parser=parser)
        f = handler.frequency
        freq_words = handler.frequency_words

        ll = 0
        tword = f[0]
        zipf = dict()
        avg = 0
        for i, num in enumerate(f):
            if num == tword:
                avg += i + 1
            else:
                zipf[freq_words[i - 1]] = tword * avg / (i - ll)
                ll = i
                avg = ll + 1
                tword = num
                if tword == 1:
                    break

        current_fields = {str(x): fields.Float for x in zipf.keys()}
        return handleIndicatorReturn(value=zipf, fields=current_fields, type='齐普夫校验')
