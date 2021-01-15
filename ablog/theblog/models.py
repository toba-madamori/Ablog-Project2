from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    title_tag = models.CharField(max_length=255, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.CharField(max_length=255, default= '')
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    snippet = models.CharField(max_length=255, default='click the link to read the full post...')
    images = models.ImageField(null= True, blank= True, upload_to='images/')


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


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, blank=True)
    profile_image = models.ImageField(null= True, blank=True, upload_to='images/profile/')
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return str(self.name) + ' | ' + str(self.body)    

    def get_absolute_url(self):
        return reverse('article-detail') 