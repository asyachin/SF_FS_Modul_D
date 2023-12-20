from django.views.generic import ListView
from .models import Author, Post, Category, Subscriber, SubscriberCategory, Comment

class AdvList(ListView):
		model = Post 
		template_name = 'ads/ads.html' 
		context_object_name = 'ads' 
		queryset = Post.objects.order_by('-created_at')
		#paginate_by = 10

		def get_queryset(self):
				return Post.objects.order_by('-created_at')