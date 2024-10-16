import pytest
from django.urls import reverse
from courses.models import Course
from rest_framework import status

@pytest.mark.django_db
class TestCourseAPI:

    def test_course_list_authenticated(self, api_client, create_user):
        user = create_user('teacher@example.com', 'password', 'TEACHER')
        api_client.force_authenticate(user=user)
        response = api_client.get(reverse('courses:course-list'))
        assert response.status_code == status.HTTP_200_OK

    def test_course_list_unauthenticated(self, api_client):
        response = api_client.get(reverse('courses:course-list'))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_course_create_by_teacher(self, api_client, create_user):
        user = create_user('teacher@example.com', 'password', 'TEACHER')
        api_client.force_authenticate(user=user)
        data = {
            'name': 'API Course',
            'description': 'Created via API',
            'availability': 'Available',
            'credits': 3,
            'maximum_capacity': 25,
            'prerequisites': []
        }
        response = api_client.post(reverse('courses:course-list'), data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Course.objects.filter(name='API Course').exists()

    def test_course_create_by_student(self, api_client, create_user):
        user = create_user('student@example.com', 'password', 'STUDENT')
        api_client.force_authenticate(user=user)
        data = {
            'name': 'Unauthorized Course',
            'description': 'Should not be created',
            'availability': 'Available',
            'credits': 3,
            'maximum_capacity': 25,
            'prerequisites': []
        }
        response = api_client.post(reverse('courses:course-list'), data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_course_detail(self, api_client, create_user):
        user = create_user('student@example.com', 'password', 'STUDENT')
        course = Course.objects.create(
            name='Detail Course',
            description='For detail view',
            availability='Available',
            credits=3,
            maximum_capacity=30
        )
        api_client.force_authenticate(user=user)
        response = api_client.get(reverse('courses:course-detail', args=[course.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Detail Course'
