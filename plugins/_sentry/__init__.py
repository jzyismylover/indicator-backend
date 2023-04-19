import sentry_sdk
import os
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk import capture_exception, capture_message

def useSentryPlugin():
  # 生产环境开启Sentry监控
  if os.path.exists('/.dockerenv'):

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

def useSentryCaptureError(error: Exception):
    capture_exception(error)

def useSentryCaptureMessage(msg: str):
    capture_message(msg)