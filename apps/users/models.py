import uuid
from django.db import models
from django.core.validators import RegexValidator


USER_TYPE ={
    "teacher":"Teacher",
    "student":"Student"
}

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField()
    birth_day = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon numarsını doğru girin.")],max_length=11, unique=True)
    user_type = models.CharField(choices=USER_TYPE)


