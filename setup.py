from flask import Flask
from flask_cors import CORS
from config import init_db, init_redis
from resources import init_views

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
sentry_sdk.init(
    dsn="https://828c3ed2282a49da8e8c58ca165e4d4e@o4504333117554688.ingest.sentry.io/4504795093008384",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

# init global params
app.config['BUNDLE_ERRORS'] = 1
CORS(app, resources={r"/*": {"origins": "*"}})

# init db
# init_db()

# init redis
redis_client = init_redis(app=app)

# init rest api
init_views(app=app)