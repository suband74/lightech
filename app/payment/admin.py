from django.contrib import admin

from payment.models import UserBalanceLog


@admin.register(UserBalanceLog)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_operation',
                    'amount', 'balance', 'created_at')
    search_fields = ('email',)
    ordering = ('-created_at',)
