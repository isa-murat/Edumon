from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.users.serializer import UserRegistrationSerializer
from apps.users.models import Users

class UserRegistrationView(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):

    serializer_class = UserRegistrationSerializer
    queryset = Users.objects.all()
