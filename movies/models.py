from django.db import models
from django.contrib.auth.models import User

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


class Movie(models.Model):
    title=models.CharField(max_length=400)
    description=models.TextField()
    created=models.DateField()
    rated=models.CharField(choices=RATINGS,max_length=1)
    duration=models.CharField(max_length=10)
    genre=models.CharField(choices=GENRE, blank=True, max_length=15)
    actors=models.CharField(max_length=400)
    country=models.CharField(max_length=100)
    type=models.CharField(choices=TYPE,max_length=15)
    poster=models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    director=models.CharField(max_length=200)
    language=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id} {self.title}'