from django.contrib import admin
from .models import Author, Post, Category, Subscriber, SubscriberCategory, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(SubscriberCategory)
admin.site.register(Comment)
