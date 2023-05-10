from flask_apscheduler import APScheduler

scheduler = APScheduler()

def init_scheduler(app):
    app.config.SCHEDULER_API_ENABLED = True
    scheduler.init_app(app)
    scheduler.start()