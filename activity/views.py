# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer
from rest_framework import generics

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Article.objects.all()
        serializer_class = ArticleDetailSerializer
