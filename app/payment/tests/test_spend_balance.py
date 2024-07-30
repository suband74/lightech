import pytest
from rest_framework import status
from django.contrib.auth import get_user_model
from payment.models import UserBalanceLog
from payment.services import UserBalanceService


@pytest.fixture
def user_2():
    user = get_user_model()
    return user.objects.create_user(
        email='email_2@mail.com', password='password_2')


@pytest.mark.django_db
def test_spend_balance(client, new_user, user_2):
    user_balance_service = UserBalanceService()
    user_balance_service.create_user_balance(user=new_user)
    user_balance_service.create_user_balance(user=user_2)

    user_balance_log = UserBalanceLog.objects.filter(
        user=new_user).latest('created_at')
    user_balance_log.balance = 400
    user_balance_log.save()

    user_balance_log_2 = UserBalanceLog.objects.filter(
        user=user_2).latest('created_at')
    user_balance_log_2.balance = 100
    user_balance_log_2.save()

    url = '/api/payment/spend/'
    payload = {
        "partner_id": user_2.id,
        "amount": 155
    }
    response = client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert UserBalanceLog.objects.count() == 4
    user_balance = UserBalanceLog.objects.filter(
        user=new_user).latest('created_at')
    user_balance_2 = UserBalanceLog.objects.filter(
        user=user_2).latest('created_at')
    assert user_balance.balance == 245
    assert user_balance_2.balance == 255
    assert response.data == {'Success': 'From your balance has been spent 155'}

    url = '/api/payment/spend/'
    payload = {
        "partner_id": user_2.id,
        "amount": 255
    }
    response = client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {'Error': 'You do not have enough money'}
