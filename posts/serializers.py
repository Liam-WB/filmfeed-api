from rest_framework import serializers
from posts.models import Post
from likes.models import Like


class OMDBSerializer(serializers.Serializer):
    title = serializers.CharField()
    actors = serializers.CharField()
    boxoffice = serializers.CharField()
    country = serializers.CharField()
    dvd = serializers.CharField()
    director = serializers.CharField()
    genre = serializers.CharField()
    language = serializers.CharField()
    metascore = serializers.CharField()
    plot = serializers.CharField()
    poster = serializers.CharField()
    production = serializers.CharField()
    rated = serializers.CharField()
    ratings = serializers.CharField()
    release = serializers.CharField()
    respone = serializers.CharField()
    runtime = serializers.CharField()
    type = serializers.CharField()
    website = serializers.CharField()
    writer = serializers.CharField()
    year = serializers.CharField()
    imdbid = serializers.CharField()
    imdbrating = serializers.CharField()
    imdbvotes = serializers.CharField()

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    movie_data = OMDBSerializer(required=False)

    def create(self, validated_data):
        movie_data = validated_data.pop('movie_data', None)
        instance = super().create(validated_data)
        if movie_data:
            instance.movie = movie_data
            instance.save()
        return instance

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'like_id', 'likes_count',
            'comments_count', 'movie_data',
        ]
