# Generated by Django 3.2.9 on 2022-03-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='disk',
            field=models.CharField(max_length=120, null=True, verbose_name='ID-DISK'),
        ),
        migrations.AddField(
            model_name='photo',
            name='name_of_user',
            field=models.CharField(max_length=120, null=True, verbose_name='username'),
        ),
    ]