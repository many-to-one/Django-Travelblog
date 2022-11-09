from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'id',
        'title',
        'author',
    )
    list_display_links = (
        'title',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
