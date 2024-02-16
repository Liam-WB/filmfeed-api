from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'post', 'created_at', 'updated_at',
            'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for Comment model used in Detail view
    Post is read only so doesn't have to be reset on each update
    """
    post = serializers.ReadOnlyField(source='post.id')