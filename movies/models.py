from django.db import models
from django.db.models import JSONField
import requests
import os
import json

if os.path.exists('env.py'):
    import env

OMDB_API_KEY = os.environ.get('OMDB_API_KEY')

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    movie_data = JSONField(null=True, blank=True)
    user_ratings = JSONField(default=list, blank=True)

    @property
    def average_rating(self):
        ratings = self.user_ratings
        if ratings:
            return sum(ratings) / len(ratings)
        return 0

    def get_movie_data(self):
        url = f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={self.title}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def save(self, *args, **kwargs):
        if not self.movie_data:
            movie_data = self.get_movie_data()
            if movie_data:
                self.movie_data = movie_data
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']