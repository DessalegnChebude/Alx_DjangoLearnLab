from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'), # Token retrival endpoint
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]

# Generate and use token 
# token retrivals 
