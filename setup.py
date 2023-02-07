from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from common import errors
from config import init_db, init_redis
from resources.common_indicator import common_indicator
from resources.Auth import Login, Regist
from resources.Language import LanguageRec

app = Flask(__name__)

# init global params
app.config['BUNDLE_ERRORS'] = 1
CORS(app, resources={r"/*": {"origins": "*"}})

# init db
db = init_db(app=app)

# init redis
redis_client = init_redis(app=app)

# init Blueprint
app.register_blueprint(common_indicator)
api = Api(app=app, errors=errors, catch_all_404s=True)

# init rest-api
api.add_resource(Login, '/auth/login')
api.add_resource(Regist, '/auth/register')
api.add_resource(LanguageRec, '/api/langrc')
