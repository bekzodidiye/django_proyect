from django.db import models
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)



class Category(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__ (self):
        return self.name

class News(models.Model):
    
    class Status(models.TextChoices):
        Draft = 'DF',"Draft"
        Published = 'Pb','Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to = 'news/images')
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    published_time = models.DateTimeField(default = timezone.now)
    created_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.Draft)
    
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("news_detail_page",args=[self.slug])

class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)

    def __str__ (self):
        return f"{self.name} - {self.email} - {self.message}"
        