from payment.models import UserBalanceLog
from user.models import User
from user.services import UserService


class UserBalanceService:
    def create_user_balance(self, user: User) -> UserBalanceLog:
        UserBalanceLog.objects.create(
            user=user,
            type_operation=UserBalanceLog.ACTIVATION,
        )

    def get_latest_user_note_by_user(self, user: User) -> None:
        return UserBalanceLog.objects.filter(user=user).latest('created_at')

    def income_user_balance(self, amount: int, email: str) -> UserBalanceLog:
        user_service = UserService()
        user = user_service.get_user_by_email(email=email)  # точно существует.
        user_balance_log = self.get_latest_user_note_by_user(user=user)
        user_latest_log_balance = user_balance_log.balance
        UserBalanceLog.objects.create(
            user=user,
            type_operation=UserBalanceLog.INCOME,
            amount=amount,
            balance=user_latest_log_balance + amount
        )

    def spend_user_balance(self, amount: int, user: User) -> None:
        user_balance_log = self.get_latest_user_note_by_user(user=user)
        user_latest_log_balance = user_balance_log.balance
        UserBalanceLog.objects.create(
            user=user,
            type_operation=UserBalanceLog.SPEND,
            amount=amount,
            balance=user_latest_log_balance - amount
        )
