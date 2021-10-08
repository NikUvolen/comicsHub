from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ComicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_complete', 'views', 'created_at', 'is_complete')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_complete',)
    list_filter = ('is_complete',)
    fields = ('title', 'description', 'is_complete', 'views', 'created_at', 'updated_at')
    readonly_fields = ('views', 'created_at', 'updated_at')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'comics_link', 'get_preview_image')
    list_display_links = ('id', 'comics_link', 'get_preview_image')
    search_fields = ('id', 'comics_id')

    def get_preview_image(self, object):
        return mark_safe(f'<img src="{object.preview_image.url}" width=75>')

    get_preview_image.short_description = 'Preview image'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_id')


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comics, ComicsAdmin)
