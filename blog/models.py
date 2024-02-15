from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='category',blank=True)
    description = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class News(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='news',blank=True)
    description = RichTextField(blank=True,null=True)
    page_views = models.IntegerField(default=0)
    is_banner =  models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'News'

    def limit_description(self):
        return self.description[:200] + '...'


class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)