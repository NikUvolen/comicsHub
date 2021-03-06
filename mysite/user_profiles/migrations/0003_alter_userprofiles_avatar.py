# Generated by Django 3.2.7 on 2021-11-10 10:43

from django.db import migrations, models
import utils.uploading


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_alter_userprofiles_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='avatar',
            field=models.ImageField(upload_to=utils.uploading.upload_function),
        ),
    ]
