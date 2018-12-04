from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta():
        model = Post
        fields = ('id', 'user', 'batch', 'description', 'image_url',)
