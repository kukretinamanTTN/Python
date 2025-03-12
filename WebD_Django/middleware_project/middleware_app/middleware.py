import logging
from django.http import HttpResponse
from django.http import HttpResponseForbidden

logger = logging.getLogger("django")

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request logged: {request.method} {request.path} from {request.META.get('REMOTE_ADDR')}")
        return self.get_response(request)


class CheckUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        logger.info(f"User-Agent: {user_agent}")
        if "bot" in user_agent.lower():
            return HttpResponse("Bots are not allowed\n", status=403)
        return self.get_response(request)


class RestrictIPMiddleware:
    BLOCKED_IPS = ["192.168.1.43"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", ""))
        if ip in self.BLOCKED_IPS:
            return HttpResponse("Access Denied: Your IP is restricted\n", status=403)
        return self.get_response(request)
