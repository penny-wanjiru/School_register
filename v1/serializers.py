from rest_framework import serializers
from .models import School, Student, Teacher, Register, Level


class SchoolSerializer(serializers.ModelSerializer):
    """School models serializer"""

    class Meta:
        fields = '__all__'
        model = School


class LevelSerializer(serializers.ModelSerializer):
    """Level model serializer"""

    class Meta:
        fields = '__all__'
        model = Level


class StudentSerializer(serializers.ModelSerializer):
    """Student model serializer."""

    class Meta:
        fields = ("name", "level")
        model = Student


class TeacherSerializer(serializers.ModelSerializer):
    """Teacher model serializer."""

    class Meta:
        fields = ('name', 'level', 'email')
        model = Teacher


class RegisterSerializer(serializers.ModelSerializer):
    """Register model serializer"""

    class Meta:
        fields = ('id', 'school', 'teacher', 'student', 'date', 'is_present')
        model = Register


class ParentStudentSerializer(StudentSerializer):
    level = LevelSerializer()


class ParentTeacherSerializer(TeacherSerializer):
    level = LevelSerializer()


class ParentRegisterSerializer(RegisterSerializer):
    teacher = TeacherSerializer()
    school = SchoolSerializer()
    student = StudentSerializer()
