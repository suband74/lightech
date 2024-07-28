from rest_framework import permissions, status, views
from rest_framework.response import Response

from user.services import UserService


class RegistrationOrAuthenticationUserView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user_service = UserService()
        user, token, created = user_service.authorize(email, password)
        if created is True:
            return Response({f'Created {user}': token}, status=status.HTTP_201_CREATED)
        elif created is False:
            return Response({f'Got {user}': token}, status=status.HTTP_200_OK)
        return Response({'Error': 'Error'}, status=status.HTTP_400_BAD_REQUEST)