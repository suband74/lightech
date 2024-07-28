import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def new_user():
    user = get_user_model()
    user_created = user.objects.create_user(
        email='email@mail.com', password='password')
    yield user_created


@pytest.fixture
def client(new_user, api_client):
    api_client.force_authenticate(user=new_user)
    yield api_client
    api_client.force_authenticate(user=None)
