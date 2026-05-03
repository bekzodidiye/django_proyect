from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(News)
class News_admin(admin.ModelAdmin):
    list_display = ['title','category','slug','published_time','status']
    list_filter = ['status','published_time','category','created_time']
    prepopulated_fields = {'slug':('title',)}
    data_hierarchy='published_time'
    search_fields = ['title','body']
    ordering = ['status','published_time']

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Contact)