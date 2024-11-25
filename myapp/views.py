from django.shortcuts import render

from rest_framework import generics
from .models import Book, Author, AreaOfExpertise
from .serializers import (
    BookSerializer, BookCreateUpdateSerializer, 
    AuthorSerializer, AreaOfExpertiseSerializer
)

# Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()

# Authors
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorCreateUpdateDeleteView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Areas of Expertise
class AreaOfExpertiseListView(generics.ListAPIView):
    queryset = AreaOfExpertise.objects.all()
    serializer_class = AreaOfExpertiseSerializer

class AreaOfExpertiseCreateUpdateDeleteView(generics.ListCreateAPIView):
    queryset = AreaOfExpertise.objects.all()
    serializer_class = AreaOfExpertiseSerializer
