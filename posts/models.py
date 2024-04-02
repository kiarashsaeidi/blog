from email.policy import default
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class tag(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.name}"



class posts(models.Model): 
    title_m = models.CharField(max_length = 10)
    title = models.CharField(max_length = 30)
    date = models.DateField(auto_now = True)    
    explain = models.CharField(max_length = 300)
    concept = models.TextField()
    image = models.ImageField(upload_to="images", default="", blank = True)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    slug = models.SlugField(default = "", blank  = True, null = False)
    tags = models.ManyToManyField(tag)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs): 
        self.slug  = slugify(self.title)
        super().save(*args, **kwargs)

    



class comment(models.Model): 
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(posts, on_delete = models.CASCADE, default = '', blank= True, null = True) 

    def __str__(self):
        return f"{self.name} {self.email}"
    

