from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserModelSerializer, UserAddressSerializer
from user_app.models import UserModel

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()