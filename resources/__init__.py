from flask_restful import Api
from resources.common_indicator import common_indicator
from resources.Auth import Login, Regist
from resources.Language import LanguageRec


def init_views(app):
    app.register_blueprint(common_indicator)
    api = Api(app=app, catch_all_404s=True)
    api.add_resource(Login, '/auth/login')
    api.add_resource(Regist, '/auth/register')
    api.add_resource(LanguageRec, '/api/langrc')
