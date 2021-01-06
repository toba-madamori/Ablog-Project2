from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import AddPostForm
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blog_post'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'   


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    #fields = '__all__'     