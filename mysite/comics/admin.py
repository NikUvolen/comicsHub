from django.contrib import admin

from .models import *


class ComicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_complete', 'views', 'created_at')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_id')


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comics, ComicsAdmin)
