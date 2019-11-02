from django.utils.deprecation import MiddlewareMixin

class MD(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "*"
        # 运行ajax的所有请求方式
        response['Access-Control-Allow-Methods'] = "*"
        return response
