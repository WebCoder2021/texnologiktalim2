from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostCategory)
admin.site.register(PostTag)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id","title",'sub_title']
    list_display_links = ('id',"title")
    prepopulated_fields = {'slug':('title',),}
    save_as = True
    group_fieldsets = True
class PostAdmin(admin.ModelAdmin):
    list_display = ["id","title",'sub_title']
    list_display_links = ('id',"title")
    prepopulated_fields = {'slug':('title',),}
    save_as = True
    group_fieldsets = True
admin.site.register(Event,EventAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(PostComment)