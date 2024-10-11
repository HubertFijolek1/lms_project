# courses/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from courses.models import Course, Schedule

User = get_user_model()


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Course 1', description='Description 1', availability='Available')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.schedule = Schedule.objects.create(course=self.course, user=self.user, start_time='2023-01-01T10:00:00Z',
                                                end_time='2023-01-01T12:00:00Z')

    def test_course_creation(self):
        self.assertEqual(self.course.name, 'Course 1')
        self.assertEqual(self.course.description, 'Description 1')
        self.assertEqual(self.course.availability, 'Available')

    def test_schedule_creation(self):
        self.assertTrue(self.schedule.start_time is not None)
        self.assertTrue(self.schedule.end_time is not None)
        self.assertEqual(self.schedule.course, self.course)
        self.assertEqual(self.schedule.user, self.user)
