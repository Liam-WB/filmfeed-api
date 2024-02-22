from rest_framework import generics, filters
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.pagination import PageNumberPagination
from .serializers import MovieSerializer  
from rest_framework.response import Response

class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        title = self.request.data.get('title')
        if title:
            movie = Movie(title=title)
            movie.save()
            serializer.instance = movie
        else:
            raise serializers.ValidationError("Title field is required.")