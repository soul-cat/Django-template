from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(max_length=5)


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
