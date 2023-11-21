from django.urls import path
from .views import NewsList, NewsDetail, news_search, news_add, news_edit, news_delete
from . import views

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),  # Matches the root URL ('/news/') and uses the NewsList view
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('search/', news_search, name='news_search'),  
    path('add/', news_add, name='news_add'),
    path('<int:pk>/edit/', news_edit, name='news_edit'),
    path('<int:pk>/delete/', news_delete, name='news_delete'), 
]