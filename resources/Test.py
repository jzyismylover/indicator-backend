import psutil
import GPUtil
from flask_restful import Resource, Api
from flask import Blueprint
from utils.json_response import make_error_response, make_success_response


class DiskCheck(Resource):
    def get(self):
        UNIT_SIZE = 1024 * 1024 * 1024  # G
        mem = psutil.virtual_memory()
        return make_success_response(
            {'memory': mem.total / UNIT_SIZE, 'percent': mem.percent}
        )


class GPUCheck(Resource):
    def get(self):
        Gpus = GPUtil.getGPUs()
        ans = []
        for gpu in Gpus:
            ans.append(
                {
                    'gpu_number': gpu.id,
                    'gpu_total': round((gpu.memoryTotal) / 1024),
                    'gpu_used': round((gpu.memoryUsed) / 1024, 2),
                    'gpu_usage': round((gpu.memoryUsed / gpu.memoryTotal) * 100, 2),
                    'gpu_free': round(gpu.memoryFree)
                }
            )

        return make_success_response(ans)


class HealthCheck(Resource):
    def get(self):
        return make_success_response('服务器运转正常')


check_model = Blueprint('check', __name__, url_prefix='/check')
check_api = Api(check_model)
check_api.add_resource(HealthCheck, '/health')
check_api.add_resource(DiskCheck, '/disk')
check_api.add_resource(GPUCheck, '/gpu')
