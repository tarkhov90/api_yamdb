from rest_framework import serializers

from reviews.models import Category, Title, Genre



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        exclude = 'id'
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = 'id'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description',
                  'genre', 'category')

class ReadTitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description',
                  'genre', 'category', 'rating',)