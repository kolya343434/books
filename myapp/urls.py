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

urlpatterns = [
    # Books
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Authors
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/manage/', AuthorCreateUpdateDeleteView.as_view(), name='author-manage'),

    # Areas of Expertise
    path('areas/', AreaOfExpertiseListView.as_view(), name='area-list'),
    path('areas/manage/', AreaOfExpertiseCreateUpdateDeleteView.as_view(), name='area-manage'),
]

from . import views

urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('documents/', views.list_documents, name='list_documents'),
]
app_name = 'myapp'
