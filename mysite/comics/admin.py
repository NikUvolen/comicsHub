from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe

from .models import *
from .forms import RequiredInlineFormSet, AtLeastOneFormSet


class ImagesInline(admin.TabularInline):

    model = Images
    readonly_fields = ('image_url',)
    formset = AtLeastOneFormSet


class ComicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_complete', 'created_at', 'is_complete', 'get_preview_image')
    list_display_links = ('id', 'title', 'get_preview_image')
    search_fields = ('id', 'title')
    list_editable = ('is_complete',)
    list_filter = ('is_complete',)
    fields = ('title', 'description', 'is_complete', 'preview_image', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    inlines = [ImagesInline]

    def get_preview_image(self, object):
        return mark_safe(f'<img src="{object.preview_image.url}" width=75>')

    get_preview_image.short_description = 'Preview image'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_id')


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Comics, ComicsAdmin)
