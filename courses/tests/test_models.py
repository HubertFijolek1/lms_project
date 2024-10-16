import pytest
from courses.models import Course
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_course_creation():
    course = Course.objects.create(
        name='Test Course',
        description='Testing course creation',
        availability='Available',
        credits=3,
        maximum_capacity=30
    )
    assert course.name == 'Test Course'
    assert course.description == 'Testing course creation'
    assert course.credits == 3
    assert course.maximum_capacity == 30
