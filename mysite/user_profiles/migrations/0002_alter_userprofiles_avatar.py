# Generated by Django 3.2.7 on 2021-11-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='avatar',
            field=models.ImageField(upload_to='photos/avatars/'),
        ),
    ]
