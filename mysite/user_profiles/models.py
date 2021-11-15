from django.contrib.auth.models import User
from django.db import models

from utils import upload_function


class UserProfiles(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/user_avatars/')

    def __str__(self):
        return self.user.username
