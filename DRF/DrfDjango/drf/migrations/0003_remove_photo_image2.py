# Generated by Django 3.2.9 on 2022-03-10 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0002_auto_20220309_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image2',
        ),
    ]
