from rest_framework import serializers
from .models import Student, Classroom


class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year', 'teacher', ]


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'gender',
                  'exam_grade', 'classroom', 'image']
