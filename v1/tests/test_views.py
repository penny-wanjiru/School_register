import datetime
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from v1.models import Person, Contacts



class SchoolAPITests(APITestCase):

    def test_create_school(self):
        """
        Test we can create a school
        """
        url = reverse('school_create')
        data = {'name': 'Gulab'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(School.objects.count(), 1)


class StudentAPITests(APITestCase):

    def test_create_student(self):
        """
        Test we can create a student
        """
        url = reverse('student_create')
        data = {'name': 'Cee'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Student.objects.count(), 1)


class TeacherAPITests(APITestCase):

    def test_create_teacher(self):
        """
        Test we can create a teacher
        """
        url = reverse('teacher_create')
        data = {'name': 'Roo'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Teacher.objects.count(), 1)
        