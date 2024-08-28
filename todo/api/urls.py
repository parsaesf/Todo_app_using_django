from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register('', TodoModelViewSet, basename='todo')
urlpatterns = router.urls