from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register('follow', FollowViewSet, basename='followers')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
