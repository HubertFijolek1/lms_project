from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomLogoutView, home
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import CustomTokenObtainPairView


ACCOUNT_LOGOUT_URL = 'accounts/logout/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home view at root URL
    path('courses/', include('courses.urls', namespace='courses')),  # Courses under '/courses/'
    path('accounts/', include('allauth.urls')),  # django-allauth URLs
    path(ACCOUNT_LOGOUT_URL, CustomLogoutView.as_view(), name='account_logout'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
