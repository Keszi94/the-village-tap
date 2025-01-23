from django.contrib import admin
from .models import Thread, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('thread', 'author', 'created_on')
    search_fields = ['content', 'thread', 'author']
    list_filter = ('created_on',)
    summernote_fields = ()


# Register your models here.
# admin.site.register(Thread)
