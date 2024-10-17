import pytest
from courses.serializers import CourseSerializer

@pytest.mark.django_db
def test_course_serializer_valid_data():
    data = {
        'name': 'Serialized Course',
        'description': 'Testing serializer',
        'availability': 'Available',
        'credits': 4,
        'maximum_capacity': 50,
        'prerequisites': []
    }
    serializer = CourseSerializer(data=data)
    assert serializer.is_valid()
    course = serializer.save()
    assert course.name == 'Serialized Course'

def test_course_serializer_invalid_data():
    data = {
        'name': '',  # Name is required
        'description': 'Testing serializer',
    }
    serializer = CourseSerializer(data=data)
    assert not serializer.is_valid()
    assert 'name' in serializer.errors
    assert 'availability' in serializer.errors
