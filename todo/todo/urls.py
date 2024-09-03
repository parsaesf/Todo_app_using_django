from .views import *
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("api-auth/", include("rest_framework.urls")),
    path("todo/", TodoListView.as_view(), name="todo-list"),
    path("todo/create/", TodoCreateView.as_view(), name="todo-create"),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo-delete"),
    path("todo/<int:pk>/edit/", TodoEditView.as_view(), name="todo-edit"),
    path("signup/", signup, name="signup"),
    path("loginn/", loginn, name="login"),
    path("signout/", signout, name="signout"),
    path("api/", include("api.urls")),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
