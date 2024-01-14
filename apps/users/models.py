import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


USER_TYPE ={
    "teacher":"Teacher",
    "student":"Student"
}

class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField()
    birth_day = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon numarsını doğru girin.")],max_length=11, unique=True)
    user_type = models.CharField(choices=USER_TYPE)
    is_staff = None
    is_active = None
    date_joined = None
    is_superuser = None
    last_login = None
    user_permissions = None
    groups = None
    class Meta:
        verbose_name = "BaseUser"
        verbose_name_plural = "BaseUsers"

class Teachers(models.Model):
    teachers_profile = models.OneToOneField(Users, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey('Students', on_delete=models.SET_NULL, null=True, related_name='teacher_student')

class Students(models.Model):
    student_profile = models.OneToOneField(Users, on_delete=models.CASCADE)
    teacher = models.OneToOneField('Teachers', on_delete=models.CASCADE, null=True, unique=True)