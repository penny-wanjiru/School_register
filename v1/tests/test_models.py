import datetime
from django.test import TestCase
from v1.models import School, Student, Teacher, Stream, Register, Form, Level


class TestSchool(TestCase):

    def test_school_creation(self):
        """Test that a school can be created"""
        school_object = School.objects.create(
            name='Nova', email='test@gmail.com', school_type='DAY', )
        self.assertEqual(school_object.name, 'Nova')
        self.assertEqual(1, School.objects.count())


class TestStream(TestCase):

    def test_stream_creation(self):
        """Test that a stream can be created"""
        stream_object = Stream.objects.create(name='A')
        self.assertEqual(stream_object.name, 'A')
        self.assertEqual(1, Stream.objects.count())


class TestForm(TestCase):

    def test_form_creation(self):
        """Test that a form can be created"""
        form_object = Form.objects.create(name='1')
        self.assertEqual(form_object.name, '1')
        self.assertEqual(1, Form.objects.count())


class TestLevel(TestCase):

    def setUp(self):
        self.stream = Stream.objects.create(name='B')
        self.form = Form.objects.create(name='2')

    def test_level_creation(self):
        """Test that a class level can be created"""
        level_object = Level.objects.create(stream=self.stream, form=self.form)
        self.assertEqual(level_object.stream.name, 'B')
        self.assertEqual(1, Level.objects.count())


class TestTeacher(TestCase):

    def setUp(self):
        self.stream = Stream.objects.create(name='B')
        self.form = Form.objects.create(name='2')
        self.level = Level.objects.create(stream=self.stream, form=self.form)

    def test_teacher_creation(self):
        """Test that a teacher can be created"""
        teacher_object = Teacher.objects.create(
            name='Mwalimu', email='test@gmail.com', level=self.level)
        self.assertEqual(teacher_object.name, 'Mwalimu')
        self.assertEqual(1, Teacher.objects.count())


class TestStudent(TestCase):

    def setUp(self):
        self.stream = Stream.objects.create(name='A')
        self.form = Form.objects.create(name='3')
        self.level = Level.objects.create(stream=self.stream, form=self.form)

    def test_student_creation(self):
        """Test that a student can be created"""
        student_object = Student.objects.create(name='Jane', level=self.level)
        self.assertEqual(student_object.name, 'Jane')
        self.assertEqual(1, Student.objects.count())


class TestRegister(TestCase):

    def setUp(self):
        self.stream = Stream.objects.create(name='C')
        self.form = Form.objects.create(name='4')
        self.level = Level.objects.create(stream=self.stream, form=self.form)
        self.student = Student.objects.create(name='John', level=self.level)

    def test_register_creation(self):
        """Test that a register can be created"""
        register_object = Register.objects.create(date=datetime.datetime.today(), student=self.student)
        self.assertEqual(register_object.student.name, 'John')
        self.assertEqual(1, Register.objects.count())
