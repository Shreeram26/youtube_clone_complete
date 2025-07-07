from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User
from .models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class VideoSerializer(serializers.ModelSerializer):
    uploader = serializers.StringRelatedField(source='user', read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_file', 'uploaded_at', 'uploader']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'video', 'content', 'timestamp']