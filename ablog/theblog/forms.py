from django import forms
from .models import Post, Category


categories = Category.objects.all().values_list('name','name')
cat = []
for item in categories:
    cat.append(item)
    


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','category', 'body', 'snippet', 'images']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices= cat, attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.TextInput(attrs={'class':'form-control'}),

        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body','snippet', 'images']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.TextInput(attrs={'class':'form-control'}),

        }        