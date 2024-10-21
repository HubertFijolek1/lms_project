from django.shortcuts import redirect

REDIRECT_URL = 'account_login'

def check_user_role(request, role):
    return request.user.is_authenticated and request.user.role == role

def role_required(required_role):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            if check_user_role(request, required_role):
                return view_func(request, *args, **kwargs)
            return redirect(REDIRECT_URL)

        return wrapped_view

    return decorator