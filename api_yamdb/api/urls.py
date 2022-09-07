from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoriesViewSet, GenreViewSet, TitleViewSet

v1_router = DefaultRouter()
v1_router.register('categories', CategoriesViewSet, basename='categories')
v1_router.register('genre', GenreViewSet, basename='genre') 
v1_router.register('title', TitleViewSet, basename='title') 
urlpatterns = [
    path('v1/', include(v1_router.urls))
]
