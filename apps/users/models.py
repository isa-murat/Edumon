import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=False,null=False, blank=False)

class Students(models.Model):
    students_profile = models.OneToOneField(Users, on_delete=models.CASCADE)
