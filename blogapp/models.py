from django.db import models
from datetime import date

# Create your models here.

class tag(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Posts(models.Model):
    
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    date = models.DateField(auto_now = True)
    excerpt = models.CharField(max_length = 200)
    image = models.CharField(max_length = 50)
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null = True)
    content = models.TextField()
    tags = models.ManyToManyField(tag)
    
