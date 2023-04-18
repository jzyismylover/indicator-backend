import os
from celery import Celery
from flask import Flask
from plugins._sentry import useSentryCaptureError


celery = Celery(
    os.environ['CELERY_NAME'],
    broker=os.environ['CELERY_BROKER_URL'],
    backend=os.environ['CELERY_RESULT_BACKEND'],
)

def init_celery(app: Flask):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):  # 创建ContextTask类并继承Celery.Task子类
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

        def on_success(self, retval, task_id, args, kwargs):
            print('异步任务运行成功')
            return super(ContextTask, self).on_success(retval, task_id, args, kwargs)
        
        def on_failure(self, exc, task_id, args, kwargs, einfo):
            print('异步任务运行失败')
            useSentryCaptureError(exc)
            return super(ContextTask, self).on_failure(exc, task_id, args, kwargs, einfo)


    celery.Task = ContextTask

    return celery
