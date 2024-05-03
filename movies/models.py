from django.db import models
from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField
import requests, os

if os.path.exists('env.py'):
    import env

OMDB_API_KEY = os.environ.get('OMDB_API_KEY')

class Movie(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    movie_data = JSONField(null=True, blank=True)
    user_ratings = models.TextField(default='[]', blank=True)

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

    def update_average_rating(self):
        ratings = json.loads(self.user_ratings)
        average_rating = sum(ratings) / len(ratings) if ratings else 0
        self.average_rating = average_rating
        self.save()

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