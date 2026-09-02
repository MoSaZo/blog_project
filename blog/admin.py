from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','created','post_status',)
    list_display_links = ('title',)
    list_filter = ('title','author','post_status',('created',JDateFieldListFilter),)
    search_fields = ('title','content',)
    ordering = ('-created',)
    readonly_fields = ('created',)
    # date_hierarchy = 'created'
    prepopulate_fields = {'slug':('title',)}
    list_editable = ('post_status',)

#admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','content','created','comment_status',)
    list_display_links = ('post',)
    list_filter = ('comment_status','created','post','author',)
    search_fields = ('author__post__content',)
    ordering = ('-created',)
    readonly_fields = ('created',)
    date_hierarchy = 'created'
    list_editable = ('comment_status',)


admin.site.register(News)
