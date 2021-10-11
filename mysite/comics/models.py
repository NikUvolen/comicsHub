from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.template.defaultfilters import escape
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from django.db import models


def user_directory_path(instance, filename):
    return f'{filename}'


# TODO: Переписать нормально модели

class Comics(models.Model):
    class Meta:
        verbose_name = 'Comics'
        verbose_name_plural = 'Comic book'
        ordering = ['-created_at']

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    preview_image = models.ImageField(upload_to='photos/',
                                      blank=False,
                                      null=False,
                                      validators=[FileExtensionValidator(allowed_extensions=['gif'])])

    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_comics', kwargs={'comics_id': self.pk})


class Images(models.Model):
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Image'

    comics_id = models.ForeignKey(Comics, on_delete=models.CASCADE, default=Comics)
    image = models.ImageField(null=True, blank=True)

    def comics_link(self):
        return mark_safe(
            f'<a href="http://127.0.0.1:8000/admin/comics/comics/{self.comics_id.pk}/change/">'
            f'{escape(self.comics_id)}'
            f'</a>')


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
