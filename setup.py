from flask import Flask
from flask_cors import CORS
from config import init_db, init_redis
from resources import init_views

app = Flask(__name__)

# init global params
app.config['BUNDLE_ERRORS'] = 1
CORS(app, resources={r"/*": {"origins": "*"}})

# init db
db = init_db(app=app)

# init redis
redis_client = init_redis(app=app)

# init rest api
init_views(app=app)