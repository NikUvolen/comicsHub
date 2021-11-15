from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.template.defaultfilters import escape
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator
from autoslug import AutoSlugField
from django.urls import reverse
from django.db import models

from utils import upload_function


def user_directory_path(instance, filename):
    return f'{filename}'


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


# TODO: Переписать нормально модели

class Comics(models.Model):
    class Meta:
        verbose_name = 'Comics'
        verbose_name_plural = 'Comic book'
        ordering = ['-created_at']

    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title', max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    preview_image = models.ImageField(upload_to=upload_function,
                                      blank=False,
                                      null=False,
                                      validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'])])

    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    def get_absolute_url(self):
        return reverse('view_comics', kwargs={'comics_slug': self.slug})


class Images(models.Model):
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Image'

    comics_id = models.ForeignKey(Comics, on_delete=models.CASCADE, default=Comics)
    image = models.ImageField(null=True, blank=True)

    def image_url(self):
        return mark_safe(f'<img src="{self.image.url}" width="auto" height="200">')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Comments(models.Model):
    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comment'
        ordering = ['-created_at']

    # path = ArrayField(models.IntegerField(), default=list)
    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comics_id = models.ForeignKey(Comics, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
