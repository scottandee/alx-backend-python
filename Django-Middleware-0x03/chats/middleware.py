from datetime import datetime
import logging

class RequestLoggingMiddleware:
    """
    This middleware logs all Requests
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)
    
    def __call__(self, request):
        user = request.user
        self.logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        response = self.get_response(request)

        return response