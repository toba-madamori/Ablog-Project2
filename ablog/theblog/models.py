from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    title_tag = models.CharField(max_length=255, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.CharField(max_length=255, default= '')
    likes = models.ManyToManyField(User, related_name='blogpost_like')


    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return(self.name)

    def get_absolute_url(self):
        return reverse('home')