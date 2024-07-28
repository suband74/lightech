from django.urls import path
from payment.views import IncomeUserBalanceView, GetUserBalance, SpendUserBalance


urlpatterns = [
    path(
        'payment/income/',
        IncomeUserBalanceView.as_view(),
    ),
    path(
        'payment/balance/',
        GetUserBalance.as_view(),
    ),
    path(
        'payment/spend/',
        SpendUserBalance.as_view(),
    ),
]
