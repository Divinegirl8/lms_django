from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=1000)
    # isbn = serializers.CharField(max_length=15)

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']
