from django.contrib import admin
from blog.models import Article, Tag
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_name', 'created_time', 'modified_time', 'author', 'is_top', 'is_show', 'post_type',)