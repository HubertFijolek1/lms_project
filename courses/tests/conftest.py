import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(email, password, role):
        return User.objects.create_user(
            email=email,
            password=password,
            role=role
        )
    return _create_user