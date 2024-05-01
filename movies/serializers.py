from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'movie_data']
        read_only_fields = ['movie_data']

    def create(self, validated_data):
        validated_data.pop('movie_data', None) # SO CAN'T BE MODIFIED - DELETE IF WANT TO MODIFY IN UPDATE
        return super().create(validated_data)