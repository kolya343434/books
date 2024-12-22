
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




from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from .models import Document
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def download_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    file_path = document.file.path

    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
        return response
    else:
        raise Http404("Файл не найден")

    # your_app/views.py
    from django.shortcuts import render
    from .models import Document

    @login_required
    def document_list(request):
        documents = Document.objects.all()
        return render(request, 'document_list.html', {'documents': documents})



@login_required
def list_documents(request):
    documents = Document.objects.all()
    return render(request, 'list_documents.html', {'documents': documents})

@login_required
def upload_document(request):
    # Ваша логика загрузки документа
    pass

@login_required
def upload_success(request):
    return render(request, 'upload_success.html')

@login_required
def download_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    file_path = document.file.path

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    else:
        raise Http404("Файл не найден")



from django.shortcuts import render
from .models import Book

# myapp/views.py
# myapp/views.py

from django.shortcuts import get_object_or_404, render
from django.http import FileResponse, Http404
from .models import Book

def book_list(request):
    print("Функция book_list вызвана")
    books = Book.objects.all()
    print(f"Количество книг: {books.count()}")  # Отладочное сообщение
    return render(request, 'myapp/book_list.html', {'books': books})

def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.file:
        raise Http404("Файл книги не найден.")
    try:
        response = FileResponse(book.file.open('rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{book.file.name.split("/")[-1]}"'
        return response
    except Exception as e:
        raise Http404(f"Ошибка при открытии файла: {str(e)}")







def home(request):
    categories = AreaOfExpertise.objects.all()  # Получаем все категории
    books = Book.objects.all()  # Опционально: получить книги для главной страницы
    context = {

        'books': books , # Если хотите отображать книги на главной
        'categories': categories
    }
    return render(request, 'myapp/home.html', context)

def upload_success(request):
    return HttpResponse("Файл успешно загружен!")

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('myapp:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'myapp/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('myapp:book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book': book})

# Добавьте остальные представления для Authors и Areas of Expertise

def upload_success(request):
    return HttpResponse("Файл успешно загружен!")


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book


def categories_list(request):
    categories = AreaOfExpertise.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'myapp/book_list.html', context)

def login_view(request):
    # Реализуйте логику для входа
    return HttpResponse("Вход")

def signup_view(request):
    # Реализуйте логику для регистрации
    return HttpResponse("Регистрация")



def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detail.html', {'book': book})


from django.shortcuts import render, get_object_or_404
from .models import Book


def book_detail(request, book_id):
    """
    Представление для отображения деталей выбранной книги.
    """
    book = get_object_or_404(Book, id=book_id)

    # Вы можете добавить дополнительную логику здесь, если необходимо

    return render(request, 'myapp/detail.html', {'book': book})

# myapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book, AreaOfExpertise

def filter_books(request):
    category_id = request.GET.get('category')  # Получаем выбранную категорию по ID
    categories = AreaOfExpertise.objects.all()  # Получаем все категории

    if category_id:
        books = Book.objects.filter(area_of_expertise__id=category_id)
    else:
        books = Book.objects.all()

    context = {
        'books': books,
        'categories': categories
    }

    return render(request, 'myapp/book_list.html', context)


from django.shortcuts import render
