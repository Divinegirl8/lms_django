from rest_framework import serializers
from .models import Book, Author, Review


class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=1000)
    # isbn = serializers.CharField(max_length=15)

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author_detail'
    # )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth', 'date_of_death']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book', 'name', 'message']
