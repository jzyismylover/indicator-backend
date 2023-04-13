from flask_restful import Api
from flask import Blueprint
from utils.jwt import check_premission
from resources.common_indicator.views import (
    TotalWords,
    DictWords,
    HapaxWords,
    Tokenizen,
    SpeechTagging,
    TTRValue,
    HPoint,
    EntropyValue,
    TCValue,
    R1Value,
    ActivityValue,
    DescriptivityValue,
    LValue,
    CurveLengthValue,
    LambdaValue,
    AdjustedModuleValue,
    GiniValue,
    R4Value,
    HapaxValue,
    WriterView,
    VerbDistance,
    RRmcValue,
    RRValue,
    SecondaryTCValue,
    ALLCommonIndicator,
)

common_indicator = Blueprint('common', __name__, url_prefix='/common')
common_api = Api(common_indicator)
common_api.add_resource(Tokenizen, '/tokenizen')
common_api.add_resource(SpeechTagging, '/tagging')
common_api.add_resource(TotalWords, '/totalWords')
common_api.add_resource(DictWords, '/dictWords')
common_api.add_resource(HapaxWords, '/hapaxWords')
common_api.add_resource(TTRValue, '/ttr')
common_api.add_resource(
    HPoint,
    '/hpoint',
)
common_api.add_resource(EntropyValue, '/entrop')
common_api.add_resource(R1Value, '/r1')
common_api.add_resource(RRValue, '/rr')
common_api.add_resource(RRmcValue, '/rrmc')
common_api.add_resource(TCValue, '/tc')
common_api.add_resource(SecondaryTCValue, '/secondtc')
common_api.add_resource(ActivityValue, '/activity')
common_api.add_resource(DescriptivityValue, '/descriptivity')
common_api.add_resource(LValue, '/lvalue')
common_api.add_resource(CurveLengthValue, '/curveLength')
common_api.add_resource(LambdaValue, '/lambda')
common_api.add_resource(AdjustedModuleValue, '/adjustModule')
common_api.add_resource(GiniValue, '/gini')
common_api.add_resource(R4Value, '/r4')
common_api.add_resource(HapaxValue, '/hapax')
common_api.add_resource(WriterView, '/writerView')
common_api.add_resource(VerbDistance, '/verbDistance')
common_api.add_resource(ALLCommonIndicator, '/all')