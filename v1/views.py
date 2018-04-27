from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import School, Student, Teacher, Register, Level
from .serializers import (SchoolSerializer, StudentSerializer,
                          TeacherSerializer, LevelSerializer,
                          RegisterSerializer, ParentStudentSerializer,
                          ParentRegisterSerializer, ParentTeacherSerializer)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permissions = (AllowAny)


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    permissions = (AllowAny)
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ParentStudentSerializer
        else:
            return self.serializer_class


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permissions = (AllowAny)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ParentTeacherSerializer
        else:
            return self.serializer_class


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permissions = (AllowAny)


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permissions = (AllowAny)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ParentRegisterSerializer
        else:
            return self.serializer_class
