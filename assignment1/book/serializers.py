from rest_framework import serializers
from book.models import Book, LANGUAGE_CHOICES, STYLE_CHOICES

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['created', 'title', 'author', 'publisher', 'publicationDate', 'numberOfPages']