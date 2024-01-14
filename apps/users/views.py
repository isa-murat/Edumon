from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import Users
from apps.users.serializer import UserSerializer

class RegisterViewSets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer




    