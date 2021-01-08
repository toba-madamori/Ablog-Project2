from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import AddPostForm, UpdatePostForm
from django.urls import reverse_lazy
import datetime
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blog_post'
    ordering = ['-date_time']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'   


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    #fields = '__all__'     

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    #fields = '__all__'    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html' 
    fields = '__all__'   
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    #form_class = AddPostForm
    template_name = 'add_category.html'
    fields = '__all__'     

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category'
    
def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats':cats, 'category_post': category_post})
