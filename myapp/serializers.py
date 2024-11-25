from rest_framework import serializers
from .models import Book, Author, AreaOfExpertise

class AreaOfExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOfExpertise
        fields = ['id', 'area']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'surname', 'name', 'patronymic']

class BookSerializer(serializers.ModelSerializer):
    area_of_expertise = AreaOfExpertiseSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'number_of_pages', 'year_of_publication', 'area_of_expertise', 'authors']

class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'number_of_pages', 'year_of_publication', 'area_of_expertise', 'authors']
