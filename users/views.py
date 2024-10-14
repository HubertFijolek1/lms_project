from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

HOME_URL = 'home'  # Extract constant


@never_cache
def user_logout_view(request):  # Renaming
    logout(request)
    return redirect(HOME_URL)  # Use constant