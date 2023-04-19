from flask import Blueprint
from flask_restful import Api
from resources.multitask.views import (
    MultiProcessCommonIndicator, 
    GetTaskLists,
    GetTaskInfo,
    DownloadTask
)

multitask_blueprint = Blueprint('multitask', __name__, url_prefix='/multi')
multitask_api = Api(multitask_blueprint)

multitask_api.add_resource(MultiProcessCommonIndicator, '/addTask')
multitask_api.add_resource(GetTaskInfo, '/getTaskInfo')
multitask_api.add_resource(GetTaskLists, '/getTasks')
multitask_api.add_resource(DownloadTask, '/downloadTask')
