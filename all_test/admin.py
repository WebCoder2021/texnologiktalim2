from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserTestResult)
admin.site.register(UserTest)
admin.site.register(TestAnswer)
admin.site.register(TestQuestion)