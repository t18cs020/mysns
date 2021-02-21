from django.contrib import admin
from .models import Posts
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(Posts)

class UserAdmin(admin.ModelAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('icon',)}),)
    list_display = ['username', 'email', 'icon']
    
admin.site.register(User, UserAdmin)