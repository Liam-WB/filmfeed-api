from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'movie_data', 'created_at', 'user_rating', 'average_rating']
        read_only_fields = ['movie_data', 'average_rating']

    def create(self, validated_data):
        validated_data.pop('movie_data', None) # SO CAN'T BE MODIFIED - DELETE IF WANT TO MODIFY IN UPDATE
        return super().create(validated_data)