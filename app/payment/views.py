from rest_framework import permissions, status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from payment.services import UserBalanceService
from payment.serializers import IncomeUserSerializer, SpendUserSerializer
from user.services import UserService


class IncomeUserBalanceView(views.APIView):
    permission_classes = [permissions.AllowAny | permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=IncomeUserSerializer,
    )
    def post(self, request):
        request_serializer = IncomeUserSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        request_serializer_data = request_serializer.validated_data
        amount = request_serializer_data.get('amount')
        email = request_serializer_data.get('email')
        user_service = UserService()
        user = user_service.get_user_by_email(email)
        user_balance_service = UserBalanceService()
        user_balance_service.income_user_balance(amount=amount, user=user)
        return Response({'Success': f'The user {email} balance has been replenished'}, status=status.HTTP_200_OK)


class GetUserBalance(views.APIView):
    def get(self, request):
        user = request.user
        user_balance_service = UserBalanceService()
        balance = user_balance_service.get_latest_user_note_by_user(
            user=user).balance
        return Response({'Your balance': f'{balance}'}, status=status.HTTP_200_OK)


class SpendUserBalance(views.APIView):
    @swagger_auto_schema(
        request_body=SpendUserSerializer,
    )
    def post(self, request):
        user = request.user
        request_serializer = SpendUserSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        request_serializer_data = request_serializer.validated_data
        amount = request_serializer_data.get('amount')
        partner_id = request_serializer_data.get('partner_id')
        user_service = UserService()
        partner = user_service.get_by_id(partner_id)
        if not partner:
            return Response({'Error': 'There is not such user'}, status=status.HTTP_400_BAD_REQUEST)
        user_balance_service = UserBalanceService()
        balance = user_balance_service.get_latest_user_note_by_user(
            user=user).balance
        if balance < amount:
            return Response({'Error': 'You do not have enough money'}, status=status.HTTP_400_BAD_REQUEST)
        user_balance_service.spend_user_balance(amount=amount, user=user)
        user_balance_service.income_user_balance(amount=amount, user=partner)
        return Response({'Success': f'From your balance has been spent {amount}'}, status=status.HTTP_200_OK)
