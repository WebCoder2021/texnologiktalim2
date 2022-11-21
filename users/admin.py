from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from users.resources import UserAdminResource
from .models import CustomUser

class PersonDetailAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name','last_name','middle_name','faculty','direction','group')
    list_filter = ['faculty','direction','group']
    search_fields = ['first_name','last_name','middle_name','faculty','direction','group']
    # list_editable = ['first_name','last_name','middle_name','faculty','direction','group']
    save_as = True
    group_fieldsets = True 
    resource_class = UserAdminResource
    
admin.site.register(CustomUser,PersonDetailAdmin)