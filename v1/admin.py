# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import School, Student, Teacher, Register, Level

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Register)
admin.site.register(Level)
