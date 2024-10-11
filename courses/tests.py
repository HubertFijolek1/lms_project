import pytest
from django.contrib.auth import get_user_model
from courses.models import Course, CourseSchedule
from users.models import UserProfile
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='Password123!')


@pytest.fixture
def course():
    return Course.objects.create(
        name='Django Basics',
        description='Learn the basics of Django framework',
        availability=True
    )


@pytest.mark.django_db
def test_course_creation(course):
    assert course.name == 'Django Basics'
    assert course.description == 'Learn the basics of Django framework'
    assert course.availability is True


@pytest.mark.django_db
def test_course_schedule_creation(user):
    course: Course = Course.objects.create(name='Math 101', description='Basic Math Course')
    start_time = timezone.now()
    end_time = start_time + timedelta(hours=2)
    course_schedule = CourseSchedule.objects.create(
        course=course,
        user=user,
        start_time=start_time,
        end_time=end_time
    )
    assert course_schedule.course == course
    assert course_schedule.user == user
    assert course_schedule.start_time == start_time
    assert course_schedule.end_time == end_time


@pytest.mark.django_db
def test_user_profile_creation(user):
    profile = UserProfile.objects.create(user=user, bio='This is a test bio.')
    assert profile.user == user
    assert profile.bio == 'This is a test bio.'