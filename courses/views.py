from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Course
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer

@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = request.user

    try:
        course.enroll_student(student)
    except ValidationError as e:
        return render(request, 'courses/enrollment_error.html', {'error': e.message})

    return redirect('courses:course_detail', course_id=course.id)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]