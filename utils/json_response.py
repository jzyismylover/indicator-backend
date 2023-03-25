# 统一返回格式
def make_error_response(data = None, msg='error', code=-1):
    return {
        'code': code,
        'data': data,
        'msg': msg
    }

def make_success_response(data = None, msg='success', code=0):
    return {
        'code': code,
        'data': data,
        'msg': msg
    }