from django.contrib import admin
from .models import UserProfiles


class UserProfilesAdmin(admin.ModelAdmin):
    fields = ('user', 'avatar',)


admin.site.register(UserProfiles, UserProfilesAdmin)
