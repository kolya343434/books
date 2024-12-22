# from django.urls import path
# from .views import (
#     BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
#     AuthorListView, AuthorCreateUpdateDeleteView,
#     AreaOfExpertiseListView, AreaOfExpertiseCreateUpdateDeleteView
# )
#
# urlpatterns = [
#     # Books
#     path('books/', BookListView.as_view(), name='book-list'),#+
#     #path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
#     #path('books/create/', BookCreateView.as_view(), name='book-create'),# ?
#     #path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
#     #path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
#
#     # Authors
#     path('authors/', AuthorListView.as_view(), name='author-list'),#+
#     #path('authors/manage/', AuthorCreateUpdateDeleteView.as_view(), name='author-manage'),
#
#     # Areas of Expertise
#     path('areas/', AreaOfExpertiseListView.as_view(), name='area-list'),#+
#     #path('areas/manage/', AreaOfExpertiseCreateUpdateDeleteView.as_view(), name='area-manage'),
# ]


# urls.py
from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    AuthorListView, AuthorCreateUpdateDeleteView,
    AreaOfExpertiseListView, AreaOfExpertiseCreateUpdateDeleteView
)

from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    AuthorListView, AuthorCreateUpdateDeleteView,
    AreaOfExpertiseListView, AreaOfExpertiseCreateUpdateDeleteView
)
from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    AuthorListView, AuthorCreateUpdateDeleteView,
    AreaOfExpertiseListView, AreaOfExpertiseCreateUpdateDeleteView
)
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Функциональное представление
    # path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Класс-представление (закомментируйте, если используете функциональное)

    path('filter/', views.filter_books, name='filter'),  # Фильтрация книг
    path('books/download/<int:book_id>/', views.download_book, name='download_book'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('categories/', views.categories_list, name='categories'),
    # Другие пути...
]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('books/', views.book_list, name='book_list'),