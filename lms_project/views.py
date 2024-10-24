from django.shortcuts import render, redirect
from django.contrib.auth import logout
from allauth.account.views import LogoutView

# Helper function to clear session and logout
def logout_and_flush_session(request):
    logout(request)  # Ensures the user session is properly cleared.
    request.session.flush()
def home(request):
    return render(request, 'home.html')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout_and_flush_session(request)
        return redirect('account_login')  # Redirects to login after logout.