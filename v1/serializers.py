from rest_framework import serializers
from .models import School, Student, Teacher, Stream, Register, Form, Level


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


class StreamSerializer(serializers.ModelSerializer):
    """Stream model serializer."""

    class Meta:
        fields = '__all__'
        model = Stream


class FormSerializer(serializers.ModelSerializer):
    """Form model serializer"""

    class Meta:
        fields = '__all__'
        model = Form


class LevelSerializer(serializers.ModelSerializer):
    """Level model serializer"""

    class Meta:
        fields = '__all__'
        model = Level


class RegisterSerializer(serializers.ModelSerializer):
    """Register model serializer"""

    class Meta:
        fields = '__all__'
        model = Register
