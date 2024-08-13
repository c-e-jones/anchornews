from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on', 'genre')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('byline', 'body')


admin.site.register(Comment)