import os
from flask import Flask
from flask_cors import CORS
from config import init_db, init_redis, init_mail
from config.db import db_session
from resources import init_views

# 生产环境开启Sentry监控
if os.path.exists('/.dockerenv'):
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
        traces_sample_rate=1.0,
    )

app = Flask(__name__)

# init global params
app.config['BUNDLE_ERRORS'] = 1
CORS(app, resources={r"/*": {"origins": "*"}})

# # init database
init_db()
# when application down; remove db-session
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# init redis
redis_client = init_redis(app=app)

# init rest-api
init_views(app=app)

# init mail instance
mail = init_mail(app)
