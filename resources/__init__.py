from flask_restful import Api
from resources.readability_indicator import readability_indicator
from resources.common_indicator import common_indicator
from resources.Language import langrc_blueprint
from resources.Test import check_model
from resources.Auth import user_blueprint
from resources.Info import info_blueprint
from resources.UserHistroy import UserHistory


def init_views(app):
    app.register_blueprint(common_indicator)
    app.register_blueprint(readability_indicator)
    app.register_blueprint(langrc_blueprint)
    app.register_blueprint(check_model)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(info_blueprint)
    api = Api(app)
    api.add_resource(UserHistory, '/getUserHistory')
