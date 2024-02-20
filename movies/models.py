from django.db import models

RATINGS=(
    ('5','5 Star'),
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

class Genre(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title=models.CharField(max_length=400)
    description=models.TextField()
    created=models.DateField()
    rated=models.CharField(choices=RATINGS,max_length=1)
    duration=models.CharField(max_length=10)
    genre=models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True,blank=True)
    actors=models.CharField(max_length=400)
    country=models.CharField(max_length=100)
    type=models.CharField(choices=TYPE,max_length=15)
    poster=models.ImageField()
    director=models.CharField(max_length=200)
    language=models.CharField(max_length=30)