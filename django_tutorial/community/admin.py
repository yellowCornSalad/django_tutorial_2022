from django.contrib import admin
from community import models


class ArticleAdmin(admin.ModelAdmin):
    # fields = ['name', 'title', 'contents', 'url', 'email', 'owner']
    fieldsets = [
        ('제목', {'fields': ['title']}),
        ('내용', {'fields': ['contents']}),
        ('작성자 정보', {'fields': ['name', 'url', 'email']}),
        ('작성자 id', {'fields': ['owner'], 'classes':['collapse']}),
    ]
    list_display = ('pk', 'title', 'url', 'cdate')
    list_filter = ['cdate']
    search_fields = ['title', 'contents']


admin.site.register(models.Article, ArticleAdmin)
