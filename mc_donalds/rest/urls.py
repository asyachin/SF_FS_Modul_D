from django.urls import path
from .views import ProductsList, ProductDetail # импортируем наше представление
 
 
 
urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),  # pk -- это первичный ключ товара, который будет выводиться у нас в шаблон
]