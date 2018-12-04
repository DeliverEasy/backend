from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

from .models import Post

# Create your views here.

@api_view(['GET'])
def post_detail(request, id):

    serializer = PostSerializer(Post.objects.get(id=id))
    return Response(serializer.data)