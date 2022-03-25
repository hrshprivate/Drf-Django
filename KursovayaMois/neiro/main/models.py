from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django_resized import ResizedImageField


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    def get_image_path(self, filename):
        path = ''.join([filename])
        return path

    fio = models.CharField('ФИО', max_length=255, default='')
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='2000-09-12')
    image = ResizedImageField(size=[500, 300], quality=100, blank=True, upload_to=get_image_path,
                              verbose_name='Картинка')

    def bit(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
        bit.short_description = 'Картинка'
        bit.allow_tags = True

