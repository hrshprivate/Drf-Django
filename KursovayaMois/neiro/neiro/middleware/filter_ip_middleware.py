from django.core.exceptions import PermissionDenied


class FilterIPMiddleware(PermissionDenied):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_ips = ['127.0.1.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip in blocked_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response