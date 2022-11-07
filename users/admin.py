from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import UserCreationForm, UserChangeForm

class BlockUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

admin.site.register(BlogUser, BlockUserAdmin)
