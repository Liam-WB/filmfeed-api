"""from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from filmfeed_api.permissions import IsOwnerOrReadOnly
from .models import Movie
from .serializers import MovieSerializer

my_api_key = 'ba89eac94d0e9dac45a1da89f74c4b50'
base_url = 'https://api.themoviedb.org/3/'

class MovieList(generics.ListCreateAPIView):
    """
    List movies or add-a-movie form if logged in
    perform_create method associates the movie with the logged in user.
    """
    template_name = 'movieapp/movies.html'
    context_object_name = 'movies'
    ordering = ['-created-at', ]
    paginate_by = 100
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    queryset = Movie.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'title',
        'genres',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def movie_poster(request, movie_id):
        url = f'{base_url}movie/{Movie.tmdb}?api_key={my_api_key}&language=en-US&page=1'
        response = requests.get(url)
        tmdb_movies = {'movieposter':response.json()}
        return render(request, 'movies.html', context=tmdb_movies)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a movie/edit or delete if you own it.
    """
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    queryset = Movie.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    """