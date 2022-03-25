import base64
import email
import io
import json
import os
import time
from datetime import date
from os import abort

from django.contrib import messages
from django.core.mail import send_mail
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status, request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

from .neiro_train import screen_from_web
from .mail import put_email, path_remover
from .main_neiro import compare_faces
from .service import PaginationRecipes
from .models import Recipe, Tag, Photo
from .serializers import RecipeSerializer, ImageSerializer
from PIL import Image
import imaplib


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginationRecipes

    @action(methods=['get'], detail=False)
    def tags(self, request):
        cats = Tag.objects.all()
        return Response({'Тэги': [c.brk for c in cats]})


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginationRecipes

    @action(methods=['POST', 'GET'], detail=False)
    def result(self, request):
        if os.path.isfile('drf/img/cam.jpg'):
            name = json.loads(request.body).get('name_of_user')
            disk = json.loads(request.body).get('disk')
            image1 = json.loads(request.body).get('image1')
            session = json.loads(request.body).get('session')
            image2 = open('drf/img/cam.jpg', 'br')
            img_bytes = base64.b64decode(image1.encode('utf-8'))
            filename = '1.jpeg'
            with open(filename, 'wb') as file_to_save:
                file_to_save.write(img_bytes)
            file = Photo.objects.filter(disk=disk, name_of_user=name)
            if file.count() >= 1:
                value = compare_faces(filename, image2)
                if value:
                    Photo.objects.create(name_of_user=name, disk=disk, date=datetime.now(), image1=filename)
                    image2.close()
                    path_remover()
                    return Response(value)
                else:
                    image2.close()
                    return Response(False)
            elif not file:
                if Photo.objects.filter(name_of_user=name).exists():
                    value = compare_faces(filename, image2)
                    email = 'lollololol686@gmail.com'
                    if value:
                        put_email(email, session)
                        image2.close()
                        Photo.objects.create(name_of_user=name, disk=disk, date=datetime.now(), image1=filename)
                        path_remover()
                        return Response(value)
                    else:
                        image2.close()
                        return Response(False)
                else:
                    value = compare_faces(filename, image2)
                    if value:
                        Photo.objects.create(name_of_user=name, disk=disk, date=datetime.now(), image1=filename)
                        image2.close()
                        path_remover()
                        return Response(value)
                    else:
                        image2.close()
                        return Response(False)
        else:
            return Response(True)

    @action(methods=['GET'], detail=False)
    def checker(self, request):
        user = screen_from_web()
        return Response(user)

    @action(methods=['GET'], detail=False)
    def del_bad_user(self, request):
        name = json.loads(request.body).get('name_of_user')
        file = Photo.objects.filter(name_of_user=name)
        copy_arr = []
        for el in file:
            copy_arr.append(el.id)
        best_id = max(copy_arr)
        bad_user = Photo.objects.get(id=best_id, name_of_user=name)
        result = bad_user.delete()
        return Response(result)






#class RecipeAPIList(generics.ListCreateAPIView):
#    queryset = Recipe.objects.all()
#    serializer_class = RecipeSerializer
#    permission_classes = [permissions.IsAuthenticated]


#class RecipeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Recipe.objects.all()
#    serializer_class = RecipeSerializer
#    permission_classes = [permissions.IsAuthenticated]




#class RecipeView(APIView):
    #def get(self, request):
        #w = Recipe.objects.all()
        #
        #   return Response({'recipes': RecipeSerializer(w, many=True).data})
    #
    #def post(self, request):
        #serializer = RecipeSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #   return Response({'recipe': serializer.data})
    #
    #def put(self, request, *args, **kwargs):
        #pk = kwargs.get("pk", None)
        #   if not pk:
    #   return Response({"error": "Method PUT not allowed"})
        #
        #try:
            #instance = Recipe.objects.get(pk=pk)
            #   except:
    #   return Response({"error": "Object does not exists"})
        #
        #serializer = RecipeSerializer(data=request.data, instance=instance)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #   return Response({"post": serializer.data})
    #
    #def delete(self, request, *args, **kwargs):
        #pk = kwargs.get("pk", None)
        #   if not pk:
    #   return Response({"error": "Method DELETE not allowed"})
        #try:
            #instance = Recipe.objects.get(pk=pk)
            #   except:
    #            return Response({"error": "Object does not exists"})
        #instance.delete()
        #        return Response({"post": "Delete post" + str(pk)})


#class RecipeView(generics.ListAPIView):
#   queryset = Recipe.objects.all()
#  serializer_class = RecipeSerializer
