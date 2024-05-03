from django.urls import path
from movies import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<str:title>/', views.MovieDetail.as_view()),
]
