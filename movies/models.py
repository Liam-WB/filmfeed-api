from django.db import models
import requests
from env import OMDB_API_KEY


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(blank=True, max_length=4)
    imdb_id = models.CharField(blank=True, max_length=20)
    plot = models.TextField(blank=True)
    poster = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp'
    )
    
    def get_movie_data(self):
        # Requests movie information, OMDB_API_KEY is replaced with imported value from env
        url = f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={self.title}'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and data.get('Response') == 'True':
            return cls(
                title=data['Title'],
                year=data['Year'],
                imdb_id=data['imdbID'],
                plot=data['Plot'],
                poster=data['Poster']
            )
        else:
            return None

    def save(self, *args, **kwargs):
        # Fetches movie data, then saves
        movie_data = self.get_movie_data()
        
        # Updates fields with data from the API's response
        self.title = movie_data.get('Title', '')

        super().save(*args, **kwargs)