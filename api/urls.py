from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from .views import current_user, UserList, post_detail, save_post, PostViewSet

urlpatterns = [
    path('token-auth/', obtain_jwt_token),
    path('token-verify/', verify_jwt_token),
    path('users/current_user/', current_user),
    path('users/users/', UserList.as_view()),
    path('post/<int:id>/', post_detail),
    path('post/list/', PostViewSet.as_view({'get': 'list'})),
    path('post/save_post/', save_post)
]
