from django import forms
from .models import Post, Category, Comment, Author

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'author', 'categories', 'news_type']
  
