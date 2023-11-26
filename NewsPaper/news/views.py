from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Post, Comment, Author # импортируем нашу модель
from django.core.paginator import Paginator
from .forms import PostForm
from django.urls import reverse_lazy

class NewsList(ListView):
    model = Post 
    template_name = 'news/news.html' 
    context_object_name = 'news' 
    queryset = Post.objects.order_by('-created_at')
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-created_at')
	
class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

def news_search(request):
    date_filter = request.GET.get('date_filter', None)
    title_filter = request.GET.get('title_filter', None)
    author_filter = request.GET.get('author_filter', None)

    queryset = Post.objects.all()

    if date_filter:
        queryset = queryset.filter(created_at__date=date_filter)
    if title_filter:
        queryset = queryset.filter(title__icontains=title_filter)
    if author_filter:
        queryset = queryset.filter(author__name__icontains=author_filter)

    context = {
        'news': queryset,
        'date_filter': date_filter,
        'title_filter': title_filter,
        'author_filter': author_filter,
    }   
    return render(request, 'news/news_search.html', context)

class NewsAdd(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'news/news_add.html'
    form_class = PostForm
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
class NewsEdit(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'news/news_edit.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('news_edit', kwargs={'pk': self.object.pk})
    
class NewsDelete(LoginRequiredMixin, DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('news_list')