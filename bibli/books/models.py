from django.db import models

class Book(models.Model):
    isbn13 = models.CharField(max_length=13, primary_key=True)
    isbn10 = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    genre = models.CharField(max_length=20)
    year = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=15)
    publisher = models.CharField(max_length=20)
    description = models.CharField(max_length=2000, null=True, blank=True)
    cover = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    authorname = models.CharField(max_length=100)

    def __str__(self):
        return self.authorname

