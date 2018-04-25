from django.db import models

class School(models.Model):
    school_types = (
        ('day', 'DAY'),
        ('boarding', 'BOARDING'),
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    school_type = models.CharField(max_length=20, choices=school_types, null=False)
    email = models.EmailField(max_length=255, blank=True)


class Stream(models.Model):
    stream_choices = (
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
        ('D', 'd'),
    )
    name = models.CharField(unique=True, max_length=200)


class Form(models.Model):
    form_choices = (
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
    )
    name = models.IntegerField(choices=form_choices)


class Level(models.Model):
    stream = models.ForeignKey(Stream, related_name='stream', on_delete=models.CASCADE)
    form = models.ForeignKey(Form, related_name='form', on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(unique=True, max_length=200)
    level = models.ForeignKey(Level, related_name='level', on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, blank=True)


class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField()
    level = models.ForeignKey(Level, related_name='level', on_delete=models.CASCADE)


class Register(models.Model):
    student = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)
    date = models.DateField()
