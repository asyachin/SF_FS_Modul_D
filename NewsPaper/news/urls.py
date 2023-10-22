from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('', NewsList.as_view()),  # Matches the root URL ('/news/') and uses the NewsList view
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
]