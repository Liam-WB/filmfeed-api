from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def create(self, request, *args, **kwargs):
        title = request.data.get('title')
        if title and Movie.objects.filter(title=title).exists():
            return Response({"error": "Movie already exists in database."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_ratings = request.data.get('user_ratings')
        if user_ratings is not None:
            instance.user_ratings.append(user_ratings)
            instance.update_average_rating()
        return super().update(request, *args, **kwargs)

class MovieSearch(APIView):
    def post(self, request, format=None):
        title = request.data.get('title')
        if title:
            movie = Movie(title=title)
            movie.save()
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Title field is required."}, status=status.HTTP_400_BAD_REQUEST)