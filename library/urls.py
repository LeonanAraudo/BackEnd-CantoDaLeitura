from django.urls import path
from .views import AuthorViewSet, BookViewSet

urlpatterns = [
    path('authors/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='author-todos'),
    path('authors/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve'}), name='author-unico'),
    path('authors/tops/', AuthorViewSet.as_view({'get' : 'requestTopAuthors'}), name='top-authors'),
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book-todos'),
    path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}), name='book-unico'),
]
