# Generated by Django 3.2.7 on 2021-11-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_alter_userprofiles_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='avatar',
            field=models.ImageField(upload_to='images/user_avatars/'),
        ),
    ]
