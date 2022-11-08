from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import BlogUserCreationForm, BlogUserChangeForm
from django.utils.safestring import mark_safe

class BlockUserAdmin(UserAdmin):
    add_form = BlogUserCreationForm
    form = BlogUserChangeForm
    list_display = (
        'get_photo',
        'username',
        'email',
        'is_admin',
    )
    list_display_links = (
        'username',
    )

    fieldsets = (
        (None, {'fields': ('username', 'photo', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_director')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('photo', 'username', 'email', 'password1', 'password2'),
        }),
    )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return '-'

admin.site.register(BlogUser, BlockUserAdmin)
