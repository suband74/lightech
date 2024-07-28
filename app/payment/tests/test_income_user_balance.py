import pytest
from rest_framework import status

from payment.models import UserBalanceLog
from payment.services import UserBalanceService


@pytest.mark.django_db
def test_income_balance(api_client, new_user):
    user_balance_service = UserBalanceService()
    user_balance_service.create_user_balance(user=new_user)
    url = '/api/payment/income/'
    payload = {
        "email": "email@mail.com",
        "amount": 155
    }
    response = api_client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert UserBalanceLog.objects.count() == 2
    user_balance = UserBalanceLog.objects.last()
    assert user_balance.balance == 155

