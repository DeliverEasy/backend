from django.http import HttpResponse
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

@api_view(['POST'])
def save_post(request):
    if request.POST:
        user = request.POST.get('user', None)
        batch = request.POST.get('batch', None)
        description = request.POST.get('description', None)
        image_file = request.POST.get('image_file', None)
        image_url = request.POST.get('image_url', None)

        newPost = Post()
        newPost.user = user
        newPost.batch = batch
        newPost.description = description
        newPost.image_file = image_file
        newPost.image_url = image_url
        newPost.save()
    return HttpResponse('')
