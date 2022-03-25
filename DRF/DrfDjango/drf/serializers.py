from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework.exceptions import ValidationError

from .models import Recipe, Photo
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class RecipeSerializer(serializers.ModelSerializer):
        author = serializers.HiddenField(default=serializers.CurrentUserDefault())

        class Meta:
            model = Recipe
            fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = "__all__"


