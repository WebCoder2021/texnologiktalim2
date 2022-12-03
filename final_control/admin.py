from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(Lesson)

from .resources import ControlAdminResource

class ControlDetailAdmin(ImportExportModelAdmin):
    list_display = ('id','question','ans',)
    list_filter = ['lesson',]
    save_as = True
    group_fieldsets = True
    resource_class = ControlAdminResource

admin.site.register(FinalControlTest,ControlDetailAdmin)
admin.site.register(ControlTest)
admin.site.register(UserControlTestResult)