# from django.shortcuts import render
#
# from rest_framework import generics
# from .models import Book, Author, AreaOfExpertise
# from .serializers import (
#     BookSerializer, BookCreateUpdateSerializer,
#     AuthorSerializer, AreaOfExpertiseSerializer
# )
#
# # Books
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookCreateUpdateSerializer
#
# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookCreateUpdateSerializer
#
# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#
# # Authors
# class AuthorListView(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
# class AuthorCreateUpdateDeleteView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
# # Areas of Expertise
# class AreaOfExpertiseListView(generics.ListAPIView):
#     queryset = AreaOfExpertise.objects.all()
#     serializer_class = AreaOfExpertiseSerializer
#
# class AreaOfExpertiseCreateUpdateDeleteView(generics.ListCreateAPIView):
#     queryset = AreaOfExpertise.objects.all()
#     serializer_class = AreaOfExpertiseSerializer

from django.shortcuts import render

from rest_framework import generics
from .models import Book, Author, AreaOfExpertise
from .serializers import (
    BookSerializer, BookCreateUpdateSerializer,
    AuthorSerializer, AreaOfExpertiseSerializer
)

# Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.select_related('area_of_expertise').prefetch_related('authors').all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.select_related('area_of_expertise').prefetch_related('authors').all()
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
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

def list_documents(request):
    documents = Document.objects.all()
    return render(request, 'list_documents.html', {'documents': documents})




def home(request):
    return render(request, 'home.html')
