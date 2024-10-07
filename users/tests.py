import pytest
from django.test import override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_registration(client):
    url = reverse('account_signup')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'Password123!',
        'password2': 'Password123!',
        'role': 'student',
    }
    response = client.post(url, data)
    assert response.status_code == 302  # Redirect after successful signup
    user = User.objects.get(username='testuser')
    assert user.email == 'test@example.com'
    assert user.role == 'student'

@override_settings(ACCOUNT_EMAIL_VERIFICATION='none')
@pytest.mark.django_db
def test_user_login(client, django_user_model):
    username = 'testuser'
    password = 'Password123!'
    user = django_user_model.objects.create_user(
        username=username, password=password
    )
    url = reverse('account_login')
    data = {'login': username, 'password': password}
    response = client.post(url, data)
    assert response.status_code == 302  # Redirect after successful login
    assert response.url == '/'


@pytest.mark.django_db
def test_user_logout(client, django_user_model):
    username = 'testuser'
    password = 'Password123!'
    user = django_user_model.objects.create_user(
        username=username, password=password
    )
    client.login(username=username, password=password)
    url = reverse('account_logout')
    response = client.post(url)
    assert response.status_code == 302  # Redirect after logout
    assert response.url == '/'
