# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer
from rest_framework import generics
from django.conf import settings
import os
import base64

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

class ArticleThumbnails(APIView):
    def get(self, request, format=None):
        thumbs=[]
        for article in Article.objects.all():
            path = str(os.path.join(settings.MEDIA_ROOT, str(article.thumbnail)))
            print(path)
            with open(path, "rb") as image_file:
                bs64_str = base64.b64encode(image_file.read())
                thumbs.append(bs64_str)
        return Response(thumbs)
