# from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Product, Order
from datetime import datetime
from django.utils import timezone
 
 
class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
   # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    ordering = ['-price'] # сортировка по цене в порядке убывания
    paginate_by = 1 # поставим постраничный вывод в один элемент
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['time_now'] = timezone.localtime(timezone.now()) # добавим переменную текущей даты time_now
       context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
       return context

# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product.html' # название шаблона будет product.html
    context_object_name = 'product' # название объекта