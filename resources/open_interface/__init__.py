from flask import Blueprint
from flask_restful import Api
from resources.open_interface.views import (
  GenerateAppId, 
  GetAppid, 
  CommonIndicatorsOpenApi,
  ReadabilityIndicatorOpenApi,
  LanguageRecognizeOpenApi,
  TextAnalyseinWordSplitOpenApi,
  TextAnalyseinTaggingOpenApi
)

open_interface_blueprint = Blueprint('open_interface', __name__)
open_interface_api = Api(open_interface_blueprint)
open_interface_api.add_resource(GenerateAppId, '/generateAppid')
open_interface_api.add_resource(GetAppid, '/getAppid')
open_interface_api.add_resource(CommonIndicatorsOpenApi, '/open/commonIndicator')
open_interface_api.add_resource(ReadabilityIndicatorOpenApi, '/open/readabilityIndicator')
open_interface_api.add_resource(LanguageRecognizeOpenApi, '/open/languageRecognize')
open_interface_api.add_resource(TextAnalyseinWordSplitOpenApi, '/open/wordSpliting')
open_interface_api.add_resource(TextAnalyseinTaggingOpenApi, '/open/wordPos')