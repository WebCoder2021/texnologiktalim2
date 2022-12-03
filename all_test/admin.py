from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


from .resources import TestQuestionDetailAdmin,TestAnswerAdminResource

class TestQuestionDetailAdmin(ImportExportModelAdmin):
    save_as = True
    group_fieldsets = True
    resource_class = TestQuestionDetailAdmin
class TestAnswerDetailAdmin(ImportExportModelAdmin):
    save_as = True
    group_fieldsets = True
    resource_class = TestAnswerAdminResource

admin.site.register(TestQuestion,TestQuestionDetailAdmin)
admin.site.register(UserTestResult)
admin.site.register(UserTest)
admin.site.register(TestAnswer,TestAnswerDetailAdmin)