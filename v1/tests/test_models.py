import datetime
from django.test import TestCase
from v1.models import School, Student, Teacher, Register, Level


class TestSchool(TestCase):

    def test_school_creation(self):
        """Test that a school can be created"""
        school_object = School.objects.create(
            name='Nova', email='test@gmail.com', school_type='DAY', )
        self.assertEqual(school_object.name, 'Nova')
        self.assertEqual(1, School.objects.count())


class TestLevel(TestCase):

    def test_level_creation(self):
        """Test that a class level can be created"""
        level_object = Level.objects.create(stream="B", form="1")
        self.assertEqual(level_object.stream, 'B')
        self.assertEqual(level_object.form, '1')
        self.assertEqual(1, Level.objects.count())


class TestTeacher(TestCase):

    def setUp(self):
        self.level = Level.objects.create(stream="C", form="1")

    def test_teacher_creation(self):
        """Test that a teacher can be created"""
        teacher_object = Teacher.objects.create(
            name='Mwalimu', email='test@gmail.com', level=self.level)
        self.assertEqual(teacher_object.name, 'Mwalimu')
        self.assertEqual(1, Teacher.objects.count())


class TestStudent(TestCase):

    def setUp(self):
        self.level = Level.objects.create(stream="C", form="1")

    def test_student_creation(self):
        """Test that a student can be created"""
        student_object = Student.objects.create(name='Jane', level=self.level)
        self.assertEqual(student_object.name, 'Jane')
        self.assertEqual(1, Student.objects.count())


class TestRegister(TestCase):

    def setUp(self):
        self.level = Level.objects.create(stream="C", form="1")
        self.school = School.objects.create(name="C", email='test@gmail.com', school_type='DAY')
        self.student = Student.objects.create(name='Jane', level=self.level)
        self.teacher = Teacher.objects.create(
            name='Mwalimu', email='test@gmail.com', level=self.level)

    def test_register_creation(self):
        """Test that a register can be created"""
        register_object = Register.objects.create(date=datetime.datetime.today(),
                                                  student=self.student, teacher=self.teacher,
                                                  school=self.school, is_present=True)
        self.assertEqual(register_object.student.name, 'Jane')
        self.assertEqual(1, Register.objects.count())
