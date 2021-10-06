from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


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

    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    images = models.ForeignKey('Images', on_delete=models.CASCADE)
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse()


class Images(models.Model):
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Image'

    preview_image = models.ImageField(upload_to=user_directory_path)
    image = models.ImageField(null=True, blank=True)


class Comments(models.Model):
    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comment'
        ordering = ['-created_at']

    # path = ArrayField(models.IntegerField(), default=list)
    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
