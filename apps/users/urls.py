from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.users import views

router = DefaultRouter()
router.register('register', views.UserRegistrationView, basename='register')

urlpatterns = []+router.urls