from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from messaging.models import User


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = User.objects.get(pk=request.user.id)
    user.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
