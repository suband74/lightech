import pytest
from rest_framework import status

from payment.models import UserBalanceLog


@pytest.mark.django_db
def test_create_user(api_client):
    url = '/api/users/authentication/'
    payload = {
        "email": "test@mail.ru",
        "password": "password*"
    }
    response = api_client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert UserBalanceLog.objects.count() == 1
    user_balance = UserBalanceLog.objects.last()
    assert user_balance.balance == 0
