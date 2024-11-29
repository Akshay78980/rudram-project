from rest_framework import serializers
from .models import Post, Comment
# from users.models import UserProfile
from users.serializers import UserProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'publication_date')

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    # author_detail = UserProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'created_at', 'comments', 'comment_count')

    def get_comment_count(self, obj):
        return obj.comments.count()