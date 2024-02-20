from django.db.models import query
from .models import Movie
from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class MovieList(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    pagination_class=PageNumberPagination
    filter_backends=[DjangoFilterBackend,]
    filterset_fields=['title','genre__name','language','type']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    lookup_field='title'
    serializer_class=MovieSerializer