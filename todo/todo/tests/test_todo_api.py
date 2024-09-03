from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from django.contrib.auth.models import User
from todo.models import TODOO


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(username="jack", password="a/@1234567")
    return user


@pytest.mark.django_db
class TestTodoApi:
    def test_get_todo_response_200_status(self, api_client, common_user):
        user = common_user
        api_client.force_authenticate(user=user)
        TODOO.objects.create(title="Test Todo", user=user)
        url = reverse("todo-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_todo_response_201_status(self, api_client, common_user):
        url = reverse("todo-list")
        data = {"title": "test", "status": TODOO.Status.in_progress}
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        print(response.status_code)
        print(response.content)
        assert response.status_code == 201

    def test_create_todo_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("todo-list")
        data = {"content": "test"}
        user = common_user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
