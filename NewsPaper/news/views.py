from typing import Any
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Category, Post, Subscriber, SubscriberCategory, Comment, Author # импортируем нашу модель
from django.core.paginator import Paginator
from .forms import PostForm
from django.urls import reverse_lazy


class AuthorRequiredMixin(PermissionRequiredMixin):
    def has_permission(self):
        # Для операций редактирования и удаления
        if 'pk' in self.kwargs:
            post = get_object_or_404(Post, pk=self.kwargs['pk'])
            return self.request.user == post.author.user or self.request.user.groups.filter(name='authors').exists()
        # Для операции добавления
        else:
            return self.request.user.groups.filter(name='authors').exists()

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        if self.request.user.is_authenticated:
            context['is_subscribed'] = SubscriberCategory.objects.filter(
                subscriber__user=self.request.user, 
                category__in=self.object.categories.all()
            ).exists()
        return context
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

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


class NewsAdd(LoginRequiredMixin, AuthorRequiredMixin, CreateView):
    model = Post
    template_name = 'news/news_add.html'
    form_class = PostForm
    success_url = reverse_lazy('news_list')
    
    def form_valid(self, form):
        form.instance.author = Author.objects.get(user=self.request.user) 
        return super().form_valid(form)
    
class NewsEdit(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Post
    template_name = 'news/news_edit.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('news_edit', kwargs={'pk': self.object.pk})
    
class NewsDelete(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('news_list')
    
@login_required
@require_POST
def subscribe(request, article_id, category_id):
    category = get_object_or_404(Category, id=category_id)
    subscriber, created = Subscriber.objects.get_or_create(user=request.user)
    SubscriberCategory.objects.get_or_create(subscriber=subscriber, category=category)
    return redirect('news_detail', pk=article_id)

@login_required
@require_POST
def unsubscribe(request, article_id, category_id):
    category = get_object_or_404(Category, id=category_id)
    subscriber = get_object_or_404(Subscriber, user=request.user)
    SubscriberCategory.objects.filter(subscriber=subscriber, category=category).delete()
    return redirect('news_detail', pk=article_id)

@login_required
def add_category_to_article(request, article_id, category_id):
    article = get_object_or_404(Post, pk=article_id)
    category = get_object_or_404(Category, pk=category_id)
    article.categories.add(category)
    return redirect('news_detail', pk=article_id)