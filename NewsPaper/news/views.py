# from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Category, Post, Comment, Author # импортируем нашу модель


class NewsList(ListView):
    model = Post # указываем модель, объекты которой мы будем выводить
    template_name = 'news/news.html' # указываем имя шаблона, в котором будет лежать html, в котором будут все посты
    context_object_name = 'news' # указываем имя переменной, которая будет хранить все объекты
    queryset = Post.objects.order_by('-created_at')
	
class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'

    def get_queryset(self):
        # Фильтруем объекты Post по свежести и сортируем их по дате публикации в убывающем порядке
        return Post.objects.order_by('-created_at')