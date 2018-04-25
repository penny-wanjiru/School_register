from django.db import models


class School(models.Model):
    school_types = (
        ('day', 'DAY'),
        ('boarding', 'BOARDING'),
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    school_type = models.CharField(max_length=20, choices=school_types, null=False)
    email = models.EmailField(max_length=255, blank=True)


class Level(models.Model):
    form_choices = (
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
    )
    stream_choices = (
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
        ('D', 'd'),
    )
    stream = models.CharField(choices=stream_choices, max_length=255)
    form = models.IntegerField(choices=form_choices)


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, blank=True)


class Register(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher)
    date = models.DateField()
    is_present = models.BooleanField()


class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    register = models.ForeignKey(Register, related_name="students")
