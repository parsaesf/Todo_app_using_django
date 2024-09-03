from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

router = DefaultRouter()
router.register("", TodoModelViewSet, basename="todo")


urlpatterns = [
    path("token/login/", CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", CustomDiscardAuthToken.as_view(), name="token-logout"),
    # login jwt
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
urlpatterns += router.urls
