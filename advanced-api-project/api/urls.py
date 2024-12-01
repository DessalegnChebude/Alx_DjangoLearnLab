from django.urls import path, include
from .views import BookList, BookDetail, AuthorList, AuthorDetail


urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'), # List and create book
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'), # Retrive, Update, Delete book.
    path('books/', BookList.as_view(), name='book-list'), # List and create book
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'), # Retrive, Update, Delete book.
]
