from django.contrib import admin
from .models import *

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','created','post_status',)
    list_filter = ('title','author','post_status','created',)
    search_fields = ('title','content',)
    ordering = ('-created',)
    prepopulate_fields = {'slug':('title',)}
    list_editable = ('post_status',)


admin.site.register(News)
admin.site.register(Comment)