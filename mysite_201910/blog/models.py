from django.db import models

# Create your models here.

class BlogPost(models.Model):
    # id is default field: id = models.IntegerField()
    title = models.TextField()
    slug = models.SlugField(unique=True, default="slug-default-title")  # hello-world-title
    content = models.TextField(null=True, blank=True)

