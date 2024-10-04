from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Set backend explicitly
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            
            # Send email confirmation
            send_confirmation_email(user, request)

            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def send_confirmation_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    confirmation_link = request.build_absolute_uri(
        reverse('confirm_email', kwargs={'uidb64': uid, 'token': token})
    )
    
    # Send email
    send_mail(
        'Confirm Your Registration',
        f'Please confirm your registration by clicking the following link: {confirmation_link}',  
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )

def confirm_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Email confirmed successfully
        return render(request, 'registration/confirmation_success.html')
    else:
        # Token invalid or expired
        return render(request, 'registration/confirmation_failed.html')