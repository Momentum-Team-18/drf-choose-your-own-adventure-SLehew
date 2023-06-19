from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Author(models.Model):
    author_last_name = models.CharField(max_length=200)
    author_first_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_last_name, ', ', self.author_first_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    FICTION = 'F'
    NON_FICTION = 'NF'
    GENRE_CHOICES = [
        (FICTION, 'fiction'),
        (NON_FICTION, 'non_fiction'),
    ]
    book_title = models.CharField(max_length=250)
    book_pages = models.IntegerField(blank=True, null=True)
    book_genre = models.CharField(choices=GENRE_CHOICES, blank=True, null=True)
    childrens_book = models.BooleanField(default=False)
    book_author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, related_name='authors_of_books')
    book_publisher = models.ForeignKey(
        to=Publisher, on_delete=models.CASCADE, related_name='publishers_of_books')
    book_featured = models.BooleanField(default=False)


class Note(models.Model):
    note_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    related_book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    user_note = models.TextField()
    note_private = models.BooleanField(default=False)


class UserLibrary(models.Model):
    READ = 'R'
    READING = 'RD'
    WANT_TO_READ = 'WR'
    BOOK_STATUS_CHOICES = [
        (READ, 'read'),
        (READING, 'reading'),
        (WANT_TO_READ, 'want_to_read'),
    ]
    library_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user_book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    book_status = models.CharField(
        choices=BOOK_STATUS_CHOICES, default=WANT_TO_READ)
    book_note = models.ForeignKey(to=Note, on_delete=models.CASCADE)
