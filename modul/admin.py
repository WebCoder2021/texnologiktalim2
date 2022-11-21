from django.contrib import admin
from .models import *
# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    list_display_links = ('id',"name")
    prepopulated_fields = {'slug':('name',),}
    save_as = True
    group_fieldsets = True
class ThemeAdmin(admin.ModelAdmin):
    list_display = ["id","title"]
    list_display_links = ('id',"title")
    prepopulated_fields = {'slug':('title',),}
    save_as = True
    group_fieldsets = True
admin.site.register(Module,ModuleAdmin)
admin.site.register(Theme,ThemeAdmin)
admin.site.register(Answer)
admin.site.register(Question)