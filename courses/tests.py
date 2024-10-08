import pytest
from courses.models import Course
from django.contrib.auth import get_user_model
from courses.models import Course, Schedule
from users.models import UserProfile
from django.utils import timezone
from datetime import timedelta

@pytest.mark.django_db
def test_course_creation():
    course = Course.objects.create(
        name='Django Basics',
        description='Learn the basics of Django framework',
        availability=True
    )
    assert course.name == 'Django Basics'
    assert course.description == 'Learn the basics of Django framework'
    assert course.availability is True



User = get_user_model()

@pytest.mark.django_db
def test_schedule_creation():
    user = User.objects.create_user(username='testuser', password='Password123!')
    course = Course.objects.create(name='Math 101', description='Basic Math Course')
    start_time = timezone.now()
    end_time = start_time + timedelta(hours=2)

    schedule = Schedule.objects.create(
        course=course,
        user=user,  
        start_time=start_time,
        end_time=end_time
    )

    assert schedule.course == course
    assert schedule.user == user
    assert schedule.start_time == start_time
    assert schedule.end_time == end_time

User = get_user_model()

@pytest.mark.django_db
def test_user_profile_creation():
    user = User.objects.create_user(username='testuser', password='Password123!')
    profile = UserProfile.objects.create(user=user, bio='This is a test bio.')

    assert profile.user == user
    assert profile.bio == 'This is a test bio.'
