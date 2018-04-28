from django.db import models


class School(models.Model):
    school_types = (
        ('day', 'DAY'),
        ('boarding', 'BOARDING'),
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    school_type = models.CharField(max_length=20,
                                   choices=school_types, null=False)
    email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.name


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
    )
    stream = models.CharField(choices=stream_choices, max_length=255)
    form = models.IntegerField(choices=form_choices)

    @property
    def name(self):
        return "%s%s" % (self.form, self.stream)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              related_name="level")
    email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Register(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name="school")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,
                                related_name="teacher")
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                related_name="student")
    date = models.DateField()
    is_present = models.BooleanField()

    def __str__(self):
        return self.date
