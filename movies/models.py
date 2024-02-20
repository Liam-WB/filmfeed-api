from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=150)
    imdb = models.CharField(max_length=50)
    tmdb = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
