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
   # path('detail/<int:book_id>/',views.detail,name='detail'),
    #path('filter/', views.filter, name='filter'),
    #path('auth/', views.auth, name='auth'),
   # path('detail/<int:book_id>/', views.detail, name='detail'),



    # Books - Class-Based Views
   # path('books/', BookListView.as_view(), name='book-list'),
    #path('', views.book_list, name='book_list'),
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('categories/', views.categories_list, name='categories'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    #path('books/create/', BookCreateView.as_view(), name='book-create'),
   # path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
   # path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Books - Function-Based Views
    path('books/download/<int:book_id>/', views.download_book, name='download_book'),
    path('upload/success/', views.upload_success, name='upload_success'),
   # path('books/', views.book_list, name='book_list'),  # Конфликт с 'book-list'

    # Authors
    #path('authors/', AuthorListView.as_view(), name='author-list'),
   # path('authors/manage/', AuthorCreateUpdateDeleteView.as_view(), name='author-manage'),

    # Areas of Expertise
    #path('areas/', AreaOfExpertiseListView.as_view(), name='area-list'),
   # path('areas/manage/', AreaOfExpertiseCreateUpdateDeleteView.as_view(), name='area-manage'),

    # Documents
    # path('', views.list_documents, name='list_documents'),  # /documents/
    # path('upload/', views.upload_document, name='upload_document'),  # /documents/upload/
   # path('upload/success/', views.upload_success, name='upload_success'),  # /documents/upload/success/
    # path('download/<int:document_id>/', views.download_document, name='download_document'),  # /documents/download/<id>/
]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('books/', views.book_list, name='book_list'),