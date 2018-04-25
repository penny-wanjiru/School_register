from rest_framework import serializers
from .models import School, Student, Teacher, Register, Level


class SchoolSerializer(serializers.ModelSerializer):
    """School models serializer"""

    class Meta:
        fields = '__all__'
        model = School


class StudentSerializer(serializers.ModelSerializer):
    """Student model serializer."""

    class Meta:
        fields = '__all__'
        model = Student


class TeacherSerializer(serializers.ModelSerializer):
    """Teacher model serializer."""

    class Meta:
        fields = '__all__'
        model = Teacher


class LevelSerializer(serializers.ModelSerializer):
    """Level model serializer"""

    class Meta:
        fields = '__all__'
        model = Level


class RegisterSerializer(serializers.ModelSerializer):
    """Register model serializer"""
    students = StudentSerializer(many=True)

    class Meta:
        fields = ('id', 'school', 'teacher', 'students', 'date', 'is_present')
        model = Register
