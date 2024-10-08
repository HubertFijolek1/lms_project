from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from allauth.account.views import LogoutView
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control


def home(request):
    return render(request, 'home.html')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def logout_view(request):
#     # your logout logic here
#     request.session.flush() 
#     return render(request, 'your_template.html')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)  # Ensures the user session is properly cleared.
        request.session.flush()  # Flushes the session data.
        return redirect('account_login')  # Redirects to login after logout.