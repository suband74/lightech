import pytest
from rest_framework import status

from payment.models import UserBalanceLog
from payment.services import UserBalanceService

@pytest.mark.django_db
def test_spend_balance(client, new_user):
    user_balance_service = UserBalanceService()
    user_balance_service.create_user_balance(user=new_user)
    user_balance_log = UserBalanceLog.objects.filter(user=new_user).latest('created_at')
    user_balance_log.balance = 400
    user_balance_log.save()
    url = '/api/payment/spend/'
    payload = {
        "email": "email@mail.com",
        "amount": 155
    }
    response = client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert UserBalanceLog.objects.count() == 2
    user_balance = UserBalanceLog.objects.last()
    assert user_balance.balance == 245
    assert response.data == {'Success': 'From your balance has been spent 155'}

    url = '/api/payment/spend/'
    payload = {
        "email": "email@mail.com",
        "amount": 255
    }
    response = client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {'Error': 'You do not have enough money'}