from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, GroupView, FollowView

app_name = 'api'

posts_router = DefaultRouter()
posts_router.register(r'posts', PostView, basename='posts')
posts_router.register(r"posts/(?P<post_id>\d+)/comments", CommentView, basename="comments")
posts_router.register(r'group', GroupView, basename='groups')
posts_router.register(r'follow', FollowView, basename='follows')

urlpatterns = [
    path('', include(posts_router.urls)),  
]

    