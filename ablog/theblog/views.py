from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import AddPostForm, UpdatePostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_time']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'   


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    #fields = '__all__'     

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    context = {'cats':cats.title().replace('-',' '), 'category_post': category_post}
    return render(request, 'category.html', context )
