from django.db import models


# Create your models here.

class Book(models.Model):
    POLITICS = 'P'
    FINANCE = 'F'
    ROMANCE = 'R'
    BOOK_CHOICES = [
        (POLITICS, 'Politics'),
        (FINANCE, 'Finance'),
        (ROMANCE, 'Romance'),
    ]
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=10)
    genre = models.CharField(max_length=1, choices=BOOK_CHOICES, default=FINANCE)


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)

