from rest_framework import serializers
from libraryAPI.models import User, Author, Publisher, Book, UserLibrary


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'author_last_name', 'author_first_name']


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ['url', 'publisher_name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'book_title', 'book_pages', 'book_genre',
                  'childrens_book', 'book_author', 'book_publisher', 'book_featured']


class UserLibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLibrary
        fields = ['url', 'library_user',
                  'user_book', 'book_status', 'book_note']
