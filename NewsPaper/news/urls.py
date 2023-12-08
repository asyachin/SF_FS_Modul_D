from django.urls import path
from .views import NewsList, NewsDetail, news_search, NewsAdd, NewsEdit, NewsDelete, add_category_to_article
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', cache_page(60)(NewsList.as_view()), name='news_list'),  # Главная страница кэшируется на 1 минуту
    path('<int:pk>/', cache_page(300)(NewsDetail.as_view()), name='news_detail'),  # Страницы новостей кэшируются на 5 минут
    path('search/', cache_page(300)(news_search), name='news_search'),  # Страница поиска кэшируется на 5 минут
    path('add/', NewsAdd.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'), 
    path('news/<int:article_id>/add_category/', add_category_to_article, name='add_category_to_article'),
    path('subscribe/<int:article_id>/<int:category_id>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:article_id>/<int:category_id>/', views.unsubscribe, name='unsubscribe'),
]