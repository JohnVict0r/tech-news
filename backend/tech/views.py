from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from tech.models import Post
from tech.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
