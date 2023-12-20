from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def update_rating(self):
        post_rating = sum([post.rating * 3 for post in self.post_set.all()])
        comment_rating = sum([comment.rating for comment in self.user.comment_set.all()])
        post_comment_rating = sum([comment.rating for post in self.post_set.all() for comment in post.comments.all()])
        
        self.rating = post_rating + comment_rating + post_comment_rating
        self.save()
        
    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField('Subscriber', through='SubscriberCategory')
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.FloatField(default=0.0)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    dislikes = models.ManyToManyField(User, related_name='disliked_posts')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.content[:124]}..."

    def __str__(self):
        return (f'Title: {self.title}'
                f'Author: {self.author}'
                f'Rating: {self.rating}'
                f'created_at: {self.created_at}'
                f'categories: {self.categories}'
                f'content: {self.content}')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
    
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.post.title} in {self.category.name}"

class SubscriberCategory(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.subscriber.user.username} subscribed to {self.category.name}"