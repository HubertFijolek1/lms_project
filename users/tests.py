import pytest
from django.test import override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Constants
USERNAME = 'testuser'
PASSWORD = 'Password123!'
EMAIL = 'test@example.com'
SIGNUP_URL = reverse('account_signup')
LOGIN_URL = reverse('account_login')
LOGOUT_URL = reverse('account_logout')


# Helper Function
def create_test_user(django_user_model, username=USERNAME, email=EMAIL, password=PASSWORD, role='student'):
    user = django_user_model.objects.create_user(username=username, password=password, email=email)
    user.role = role
    user.save()
    return user


@pytest.mark.django_db
def test_user_registration(client):
    data = {
        'username': USERNAME,
        'email': EMAIL,
        'password1': PASSWORD,
        'password2': PASSWORD,
        'role': 'student',
    }
    response = client.post(SIGNUP_URL, data)
    assert response.status_code == 302  # Redirect after successful signup
    user = User.objects.get(username=USERNAME)
    assert user.email == EMAIL
    assert user.role == 'student'


@override_settings(ACCOUNT_EMAIL_VERIFICATION='none')
@pytest.mark.django_db
def test_user_login(client, django_user_model):
    create_test_user(django_user_model)
    data = {'login': USERNAME, 'password': PASSWORD}
    response = client.post(LOGIN_URL, data)
    assert response.status_code == 302  # Redirect after successful login
    assert response.url == '/'


@pytest.mark.django_db
def test_user_logout(client, django_user_model):
    create_test_user(django_user_model)
    client.login(username=USERNAME, password=PASSWORD)
    response = client.post(LOGOUT_URL)
    assert response.status_code == 302  # Redirect after logout
    assert response.url == '/'