import torch
from flask import Flask
from flask_cors import CORS
from config import init_db, init_redis, init_mail, init_celery, init_scheduler
from resources import init_views

# 上报错误到 sentry
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration

# sentry_sdk.init(
#     dsn="https://d3673c0057c04c4aabff0b247a8df395@o4505237079064576.ingest.sentry.io/4505237080834048",
#     # integrations=[
#     #     FlaskIntegration(),
#     # ],

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0
# )

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = 1
CORS(app, resources={r"/*": {"origins": "*"}})

init_views(app)
init_db(app)
init_mail(app)
init_redis(app)
celery = init_celery(app)

init_scheduler(app)

@app.teardown_appcontext
def clearGPU(exception=None):
  torch.cuda.empty_cache()

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0