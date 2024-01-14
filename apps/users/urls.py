from django.urls import path,include
from rest_framework import routers
from apps.users.views import RegisterViewSets

router = routers.DefaultRouter()
router.register(r'register',RegisterViewSets)



urlpatterns = [

]+router.urls