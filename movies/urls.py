from django.urls import path
from movies import views
from .views import MovieSearch

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:pk>/', views.MovieDetail.as_view()),
    path('search/', MovieSearch.as_view(), name='movie-search'),
]
