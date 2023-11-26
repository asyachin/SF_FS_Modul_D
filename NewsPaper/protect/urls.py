from django.urls import path
from .views import IndexView
from sign.views import upgrade_me


app_name = 'protect'

urlpatterns = [
    path('', IndexView.as_view()),
    path('upgrade/', upgrade_me, name = 'upgrade')
]