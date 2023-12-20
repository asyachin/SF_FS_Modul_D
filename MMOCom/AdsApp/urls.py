from django.urls import path
from . import views

app_name = 'AdsApp'

urlpatterns = [

	path('', views.AdvList.as_view(), name='ads_list'),
	#path('ads/<int:pk>/', views.AdvertisementDetailView.as_view(), name='ads_detail'),
	#path('ads/create/', views.AdvertisementCreateView.as_view(), name='ads_create'),
	#path('ads/<int:pk>/update/', views.AdvertisementUpdateView.as_view(), name='ads_update'),
	#path('ads/<int:pk>/delete/', views.AdvertisementDeleteView.as_view(), name='ads_delete'),
	#path('ads/<int:pk>/response/create/', views.ResponseCreateView.as_view(), name='response_create'),
]