from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    tome = models.IntegerField()
    subtitle = models.CharField(max_length=255, blank=True)
    author_first_name = models.CharField(max_length=255, blank=True)
    author_last_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    subgenre = models.CharField(max_length=50)
    nbpages = models.IntegerField()
    editor = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    imagepath = models.CharField(max_length=200, blank=True)

    def __str__(self):
        full_title = self.title
        if self.tome > 0:
            full_title = full_title + " Tome " + str(self.tome)
        if self.subtitle:
            full_title = full_title + " - " + self.subtitle
        return full_title

    def author(self):
        return self.author_first_name + " " + self.author_last_name


class Shelf(models.Model):
    sheight = models.IntegerField()
    slength = models.IntegerField()
    sdepth = models.IntegerField()

