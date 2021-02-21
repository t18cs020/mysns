from django.contrib import admin
from .models import Posts
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Posts)

class UserInfoAdmin(admin.ModelAdmin):

    def icon_image(self, obj):
        return mark_safe('<img src="{}" style="width:80px;height:auto;">'.format(obj.user_icon.url))

    list_display = ('username', 'icon_image')
    
admin.site.register(User, UserAdmin)