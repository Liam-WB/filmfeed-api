from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    movie_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']