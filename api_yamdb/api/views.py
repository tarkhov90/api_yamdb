from django.shortcuts import render
from django.db.models import Avg
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import CategorySerializer, GenreSerializer, TitleSerializer, ReadTitleSerializer

from reviews.models import Category, Genre, Title 

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    serializer_class = TitleSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TitleSerializer
        return ReadTitleSerializer