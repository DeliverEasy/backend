from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Post

'''
class PostSerializer(serializers.ModelSerializer):

    class Meta():
        model = Post
        fields = ('id', 'user', 'batch', 'description', 'image_url',)
'''


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'image_url',
        )


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'description',
            'product_name',
            'product_type',
            'quantity',
            'stock',
            'product_description',
            'brand',
            'image_url',
        )
