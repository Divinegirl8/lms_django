from django.db import models
from uuid import uuid4

from libraryManagementDjango import settings


# Create your models here.
class BookImage(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE, related_name='book_image')
    img_field = models.ImageField(upload_to='')


class BookUser(models.Model):
    pass


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    # POLITICS = 'P'
    # FINANCE = 'F'
    # ROMANCE = 'R'
    # BOOK_CHOICES = [
    #     (POLITICS, 'Politics'),
    #     (FINANCE, 'Finance'),
    #     (ROMANCE, 'Romance'),
    # ]
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=15)
    genre = models.ManyToManyField(Genre, related_name='books')
    # genre = models.CharField(max_length=1, choices=BOOK_CHOICES, default=FINANCE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


    def list_genre(self):
        return ','.join(genre.name for genre in self.genre.all()[:2])

    def __str__(self):
        return f'{self.title} {self.isbn} {self.summary} {self.list_genre()}'


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.date_of_birth} {self.date_of_death}'


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class BookInstance(models.Model):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'

    STATUS_CHOICES = [
        ('A', 'AVAILABLE'),
        ("U", 'UNAVAILABLE')
    ]
    unique_id = models.UUIDField(default=uuid4, primary_key=True)
    due_back = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.unique_id} {self.due_back} {self.status}'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'{self.name} {self.message} {self.book}'
