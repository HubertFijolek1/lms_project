from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache

@never_cache
def logout_view(request):
    logout(request)
    return redirect('home')