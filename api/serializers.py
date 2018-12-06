from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from users.models import DeliverUser
from delivermodels.models import Post

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliverUser
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = DeliverUser
        fields = ('token', 'username', 'password')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'image_url',
            'stock'
        )


class PostDetailSerializer(serializers.ModelSerializer):
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