from django.db import models
from django.contrib.auth.models import User
import requests
from env import OMDB_API_KEY


"""
RATINGS=(
    ('5', '5 Star'),
    ('4', '4 Star'),
    ('3', '3 Star'),
    ('2', '2 Star'),
    ('1', '1 Star'),
)

TYPE=(
    ('movie','movie'),
    ('series','series'),
    ('episode','episode'),
)

GENRE=(
    ('Action','Action'),
    ('Horror','Horror'),
    ('Comedy','Comedy'),
    ('Drama','Drama'),
    ('Fantasy','Fantasy'),
    ('Thriller','Thriller'),
    ('Romance','Romance'),
    ('Western','Western'),
    ('Adventure','Adventure'),
    ('Science fiction','Science fiction'),
    ('Crime','Crime'),
    ('Animation','Animation'),
    ('Documentary','Documentary'),
    ('Mystery','Mystery'),
    ('History','History'),
    ('Sports','Sports'),
    ('Musical','Musical'),
    ('News','News'),
)
"""


class Movie(models.Model):
    title=models.CharField(max_length=400)

    def get_movie_data(self):
        url = f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={self.title}'
        response = requests.get(url)
        data = response.json()
        return data

    def save(self, *args, **kwargs):
        # Fetches movie data, then saves
        movie_data = self.get_movie_data()
        
        # Updates fields with data from the API's response
        self.title = movie_data.get('Title', '')
        
        super().save(*args, **kwargs)