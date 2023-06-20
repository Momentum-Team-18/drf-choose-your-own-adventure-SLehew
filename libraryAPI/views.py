from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from libraryAPI.models import User, Author, Publisher, Book, UserLibrary
from libraryAPI.serializers import UserSerializer, AuthorSerializer, PublisherSerializer, BookSerializer, UserLibrarySerializer


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


class UserLibraryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = UserLibrary.objects.all()
    serializer_class = UserLibrarySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['library_user', 'user_book', 'book_status', 'book_note']

    def get_queryset(self):
        """
        This view should return a list of all the books
        for the currently authenticated user.
        """
        queryset = UserLibrary.objects.filter(user=self.request.user)
        return queryset
