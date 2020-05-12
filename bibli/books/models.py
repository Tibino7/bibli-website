from django.db import models

class Book(models.Model):
    isbn13 = models.CharField(max_length=13)
    isbn10 = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    year = models.IntegerField
    language = models.CharField(max_length=15)
    publisher = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)

class AuthorBooks(models.Model):
    id = models.IntegerField
    author = models.CharField(max_length=100)
    bookisbn13 = models.CharField(max_length=13)

