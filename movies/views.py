from rest_framework import generics, filters
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response


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

class MovieDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a movie.
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()