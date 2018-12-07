from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, PostSerializer, PostDetailSerializer
from delivermodels.models import Post, DeliverUser

# Create your views here.

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_detail(request, id):
    serializer = PostDetailSerializer(Post.objects.get(id=id))
    return Response(serializer.data)


@api_view(['POST'])
def save_post(request):
    user = DeliverUser.objects.get(id=request.user.id)
    product_name = request.POST.get('product_name')
    product_description = request.POST.get('product_description')
    title = request.POST.get('title')
    product_type = request.POST.get('product_type')
    brand = request.POST.get('brand')
    description = request.POST.get('description')
    image_url = request.POST.get('image_url')
    quantity = request.POST.get('quantity')
    stock = request.POST.get('stock')

    newPost = Post()
    newPost.user = user
    newPost.product_name = product_name
    newPost.product_description = product_description
    newPost.title = title
    newPost.product_type = product_type
    newPost.brand = brand
    newPost.description = description
    newPost.image_url = image_url
    newPost.quantity = quantity
    newPost.stock = stock
    newPost.save()
    return HttpResponse(status=201)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer