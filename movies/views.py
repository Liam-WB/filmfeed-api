"""from django.db.models import query"""
from .models import Movie
"""from django.shortcuts import render"""
from rest_framework import generics, filters
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MovieList(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        ]
    search_fields = ['title', 'year']
    ordering_fields = ['title', 'year']
    filterset_fields=['title',]

    def perform_create(self, serializer):
        title = self.request.data.get('title')
        movie = Movie.create_from_api(title)
        if movie:
            serializer.save(
                title=movie.title,
                year=movie.year,
                imdb_id=movie.imdb_id,
                plot=movie.plot,
                poster=movie.poster
            )
        else:
            serializer.validated_data['error'] = 'Movie not found'


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer