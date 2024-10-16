from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    prerequisites = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all()
    )

    class Meta:
        model = Course
        fields = '__all__'

    def validate(self, data):
        if data['maximum_capacity'] <= 0:
            raise serializers.ValidationError("Maximum capacity must be greater than zero.")
        return data