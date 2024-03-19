from django.db import models
from django.db.models import JSONField
import requests, os

# TEMPORARY MODEL

if os.path.exists('env.py'):
    import env

OMDB_API_KEY = os.environ.get('OMDB_API_KEY')

class Movie(models.Model):
    title = models.CharField(max_length=255)
    movie_data = JSONField(null=True, blank=True)

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
        movie_data = self.get_movie_data()
        
        if movie_data:
            self.movie_data = movie_data
            if 'Title' in movie_data:
                self.title = movie_data.get('Title', '')
                super().save(*args, **kwargs)
            else:
                print("Error: Movie requires all data to save.")
        else:
            print("Error: Movie not found.")