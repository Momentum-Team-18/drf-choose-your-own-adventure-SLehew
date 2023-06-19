from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from libraryAPI.models import User, Author, Publisher, Book
from libraryAPI.serializers import UserSerializer, AuthorSerializer, PublisherSerializer, BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author_last_name', 'author_first_name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['publisher_name']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
