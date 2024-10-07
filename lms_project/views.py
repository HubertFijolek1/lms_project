from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache

def home(request):
    return render(request, 'home.html')

@never_cache
def logout_view(request):
    logout(request)
    return redirect('home')