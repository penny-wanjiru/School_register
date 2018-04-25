# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import School, Student, Teacher, Stream, Register, Form
admin.site.register(School)
