from djongo import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Book(models.Model):
    isbn13 = models.CharField(max_length=13, primary_key=True)
    isbn10 = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=255)
    authors = models.ArrayField(
        model_container = Author,
    )
    genre = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=2)
    publisher = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.CharField(max_length=255, null=True, blank=True)
