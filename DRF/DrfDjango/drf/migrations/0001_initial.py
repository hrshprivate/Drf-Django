# Generated by Django 3.2.9 on 2022-03-07 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import drf.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Шо')),
                ('mass', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество')),
                ('Value', models.CharField(max_length=100, null=True, verbose_name='Имя рецепта')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ингридиенты',
                'verbose_name_plural': 'Ингридиенты',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', django_resized.forms.ResizedImageField(crop=None, default='pictures/def.jpg', force_format=None, keep_meta=True, quality=100, size=[500, 300], upload_to=drf.models.Photo.get_image_path, verbose_name='Картинка')),
                ('image2', django_resized.forms.ResizedImageField(crop=None, default='pictures/def.jpg', force_format=None, keep_meta=True, quality=100, size=[500, 300], upload_to=drf.models.Photo.get_image_path, verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Картинки',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='Название')),
                ('dis', models.TextField(verbose_name='Desc:')),
                ('time', models.IntegerField(null=True, verbose_name='Время')),
                ('image', django_resized.forms.ResizedImageField(crop=None, default='pictures/def.jpg', force_format=None, keep_meta=True, quality=100, size=[500, 300], upload_to=drf.models.Recipe.get_image_path, verbose_name='Картинка')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
                ('ing', models.ManyToManyField(blank=True, related_name='ing', to='drf.Ing')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brk', models.CharField(max_length=10, null=True, verbose_name='Время дня и ночи')),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='подписчик')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
            },
        ),
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoplist', to='drf.recipe', verbose_name='рецепты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoplist', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'список покупок',
                'verbose_name_plural': 'списки покупок',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag', to='drf.Tag'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_recipes', to='drf.recipe', verbose_name='рецепт в избранном')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'избранное',
                'verbose_name_plural': 'избранное',
            },
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_subscription'),
        ),
        migrations.AddConstraint(
            model_name='shoplist',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_shoplist'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('recipe', 'user'), name='UniqueFavorite'),
        ),
    ]
