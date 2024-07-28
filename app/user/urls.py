from django.urls import path
from user.views import RegistrationOrAuthenticationUserView


urlpatterns = [
    path(
        'users/authentication/',
        RegistrationOrAuthenticationUserView.as_view(),
    ),
]
