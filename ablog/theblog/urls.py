
from django.urls import path
from theblog import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryListView, CategoryView, BlogPostLike

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail' ),
    path('add_post', AddPostView.as_view(), name= 'add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name= 'update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name= 'delete_post'),
    path('add_category', AddCategoryView.as_view(), name= 'add_category'),
    path('category', CategoryListView.as_view(), name= 'category_list'),
    path('category_body/<str:cats>', CategoryView, name= 'category_body'),
    path('blogpost-like/<int:pk>', BlogPostLike, name= 'blogpost_like'),

]
