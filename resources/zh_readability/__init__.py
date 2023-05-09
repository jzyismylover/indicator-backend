from flask import Blueprint
from flask_restful import Api
from resources.zh_readability.views import Feature18Main, Feature22Main

zh_readability_blueprint = Blueprint('zh_readability', __name__, url_prefix='/zh_readability')
zh_readability_api = Api(zh_readability_blueprint)
zh_readability_api.add_resource(Feature18Main, '/feature18')
zh_readability_api.add_resource(Feature22Main, '/feature22')