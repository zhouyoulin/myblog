from django.contrib import admin
from . import models

# Register your models here.
class BlogArticleAdim(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['publish','author']

admin.site.register(models.BlogArticle, BlogArticleAdim)