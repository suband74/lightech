import pytest
from rest_framework import status

from payment.models import UserBalanceLog
from payment.services import UserBalanceService

@pytest.mark.django_db
def test_get_balance(client, new_user):
    user_balance_service = UserBalanceService()
    user_balance_service.create_user_balance(user=new_user)
    user_balance_log = UserBalanceLog.objects.filter(user=new_user).latest('created_at')
    user_balance_log.balance = 400
    user_balance_log.save()
    url = '/api/payment/balance/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'Your balance': '400'}