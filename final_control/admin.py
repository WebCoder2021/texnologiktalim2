from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


from .resources import ControlAdminResource

class ControlDetailAdmin(ImportExportModelAdmin):
    list_display = ('id','question','ans','ans1','ans2','ans3',)
    # list_editable = ('question','ans','ans1','ans2','ans3',)
    list_filter = ['lesson',]
    save_as = True
    group_fieldsets = True
    resource_class = ControlAdminResource
class LessonAdmin(ImportExportModelAdmin):
    list_display = ('id','name',)
admin.site.register(FinalControlTest,ControlDetailAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(ControlTest)
class UserControlTestResultAdmin(ImportExportModelAdmin):
    list_display = ('id','user','lesson','result','is_trues')
    # list_editable = ('question','ans','ans1','ans2','ans3',)
    list_filter = ['user','lesson']
    save_as = True
admin.site.register(UserControlTestResult,UserControlTestResultAdmin)