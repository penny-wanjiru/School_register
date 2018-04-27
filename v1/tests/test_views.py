import datetime
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from v1.models import School, Teacher, Student, Level


class SchoolAPITests(APITestCase):

    def test_create_school(self):
        """
        Test we can create a school
        """
        response = self.client.post(
            '/api/v1/schools/',
            {'name': 'St.Catherines', 'school_type': 'boarding',
             'email': 'zipping@gmail.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(School.objects.count(), 1)


class StudentAPITests(APITestCase):
    def setUp(self):
        self.level = Level.objects.create(stream="A", form="1")

    def test_create_student(self):
        """
        Test we can create a student
        """
        response = self.client.post(
            '/api/v1/students/',
            {'name': 'Eli', 'level': 1})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Student.objects.count(), 1)


class TeacherAPITests(APITestCase):

    def setUp(self):
        self.level = Level.objects.create(stream="B", form="1")

    def test_create_teacher(self):
        """
        Test we can create a teacher
        """
        response = self.client.post(
            '/api/v1/teachers/',
            {'name': 'Mr.Popo', 'level': 1,
             'email': 'teach@gmail.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Teacher.objects.count(), 1)
