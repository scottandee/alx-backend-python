from datetime import datetime, time
import logging
from django.utils import timezone
from rest_framework import status
from django.http import JsonResponse

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

class RestrictAccessByTimeMiddleware:
    """
    This middleware restricts access to the chat
    outside 9pm and 6pm
    """

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        curr_time = timezone.now().time()
        if not (curr_time > time(hour=18) and curr_time < time(hour=21)):
            return JsonResponse(
                {'error': 'Chat is restricted at this time'},
                status=status.HTTP_403_FORBIDDEN
            )

        response = self.get_response(request)

        return response

class OffensiveLanguageMiddleware:
    """
    This middleware tracks the number of chat messages sent by
    each ip address and implements a 5 message per limit
    timeline.
    """
    ips = {}

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        response = self.get_response(request)

        return response

class RolepermissionMiddleware:
    """
    This middleware tracks checks the users role from the
    request and if the user is not admin or moderator,
    it returns error 403
    """

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        response = self.get_response(request)

        return response
        