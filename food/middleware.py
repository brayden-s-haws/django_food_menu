import time
from django.http import HttpResponseForbidden


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # process before the view
        print(f"[Middleware] Request Path: {request.path}")
        response = self.get_response(request)
        # process after the view
        print(f"[Middleware] Response Status: {response.status_code}")
        return response

class TimeRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        process_time = time.time() - start_time
        print(f"[Middleware] Process Time: {process_time:.2f}seconds")
        return response

class BlockIPMiddleware:
    BLOCKED_IPS = []
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.BLOCKED_IPS:
            return HttpResponseForbidden('<h1>Forbidden</h1>')
        return self.get_response(request)
