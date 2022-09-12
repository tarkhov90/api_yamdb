from api.views import (CategoriesViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet, code, signup,
                       token)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('categories', CategoriesViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'),

authpatterns = [
    path('signup/', signup, name='signup'),
    path('token/', token, name='login'),
    path('code/', code, name='code')
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include(authpatterns))
]
