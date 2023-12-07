from django.urls import path
from .views import NewsList, NewsDetail, news_search, NewsAdd, NewsEdit, NewsDelete, add_category_to_article
from . import views

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),  # Matches the root URL ('/news/') and uses the NewsList view
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('search/', news_search, name='news_search'),  
    path('add/', NewsAdd.as_view(), name='news_add'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'), 
    path('news/<int:article_id>/add_category/', add_category_to_article, name='add_category_to_article'),
    path('subscribe/<int:article_id>/<int:category_id>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:article_id>/<int:category_id>/', views.unsubscribe, name='unsubscribe'),
]