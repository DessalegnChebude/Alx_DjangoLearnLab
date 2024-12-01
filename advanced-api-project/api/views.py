from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, filters
from .permission import IsAuthorOrReadOnly

# Create your views here.

# View to create a new author with permission checks and custom validations.
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def create_author(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    # View to update an author with custom validations and permission checks.    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def update_author(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        author = self.get_object()
        serializer = self.get_serializer(author, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# 
class BookList(generics.ListCreateAPIView):
    # this class is used to View a list of all books and create a new book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name'] # This will allow to filter books by their title and author name.
    
    def get_queryset(self):
        """
        Optionally restricts the returned books to a given author,
        by filtering against an `author_id` query parameter in the URL.
        """
        queryset = Book.objects.all()
        # Access query_params from the request
        author_id = self.request.query_params.get('author_id', None)
        if author_id is not None:
            queryset = queryset.filter(author__id=author_id)
        return queryset
    
    def create_book(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    # This BookDetail class view used to retrieve, update, or delete a book instance.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def update_book(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data, partial=partial)
        serializer.is_valid(raise_excepption=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

