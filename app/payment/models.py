from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserBalanceLog(models.Model):
    ACTIVATION = 'activation'
    INCOME = 'income'
    SPEND= 'spend'

    TYPES = [
        (ACTIVATION, _('Activation')),
        (INCOME, _('Income')),
        (SPEND, _('Spend')),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        db_index=True,
    )
    type_operation = models.CharField(
        max_length=20,
        choices=TYPES,
        default=INCOME,
    )
    amount = models.PositiveBigIntegerField(_('Amount'), default=0)
    balance = models.PositiveBigIntegerField(_('Balance'), default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = _('Balance Operation Log')
        verbose_name_plural = _('Balance Operation Logs')

    def __str__(self):
        return f'Balance Operation: {self.user}/{self.amount}/{self.type_operation}'
