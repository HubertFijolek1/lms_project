from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import CustomLogoutView, home

ACCOUNT_LOGOUT_URL = 'accounts/logout/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('courses/', include('courses.urls', namespace='courses')),
    path('accounts/', include('allauth.urls')),  # django-allauth URLs
    path(ACCOUNT_LOGOUT_URL, CustomLogoutView.as_view(), name='account_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)