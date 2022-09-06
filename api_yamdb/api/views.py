from django.shortcuts import render
from .models import Review, Comment, Title
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import (CommentSerializer, ReviewSerializer)
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
# Create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
   
    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
   
    def get_queryset(self):
        review = get_object_or_404(Comment, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, review=review)   
