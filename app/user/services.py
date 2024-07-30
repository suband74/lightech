from rest_framework_jwt.settings import api_settings
from user.models import User


class UserService:
    def authorize(self, email: str, password: str) -> tuple[User, str, bool]:
        user = User.objects.filter(email=email).first()
        created = False
        if user is None:
            user = User.objects.create_user(email, password)
            created = True
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return user, token, created

    def get_user_by_email(self, email: str) -> User | None:
        return User.objects.filter(email=email).first()

    def get_by_id(self, id: int) -> User | None:
        return User.objects.filter(pk=id).first()
