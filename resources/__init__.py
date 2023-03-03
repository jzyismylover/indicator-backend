from flask_restful import Api
from resources.readability_indicator import readability_indicator
from resources.common_indicator import common_indicator
from resources.Auth import Login, Regist
from resources.Language import langrc_blueprint


def init_views(app):
    app.register_blueprint(common_indicator)
    app.register_blueprint(readability_indicator)
    app.register_blueprint(langrc_blueprint)
    api = Api(app=app, catch_all_404s=True)
    api.add_resource(Login, '/auth/login')
    api.add_resource(Regist, '/auth/register')
