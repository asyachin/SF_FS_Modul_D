from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Author, Post, SubscriberCategory
from django.core.mail import send_mail
from django.template.loader import render_to_string

@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.get_or_create(user=instance)
        
        
@receiver(post_save, sender=SubscriberCategory)
def send_subscription_confirmation_email(sender, instance, created, **kwargs):
    if created:
        user = instance.subscriber.user
        category = instance.category
        subject = f'Подписка на категорию {category.name}'
        message = f'Здравствуй, {user.username}. Ты успешно подписался на обновления в категории "{category.name}"!'
        html_message = render_to_string('subscriptions/subscription_confirmation_email.html', {
            'user': user,
            'category': category
        })
        send_mail(subject, message, 'subscription@newsagg.com', [user.email], html_message=html_message)
        
@receiver(post_save, sender=Post)
def send_new_post_notification(sender, instance, created, **kwargs):
    if created:
        for category in instance.categories.all():
            subscribers = SubscriberCategory.objects.filter(category=category)
            for subscriber in subscribers:
                user = subscriber.subscriber.user
                subject = instance.title
                html_message = render_to_string('subscriptions/new_post_notification.html', {
                    'post': instance,
                    'user': user
                })
                subject_message = f'Здравствуй, {user.username}. Новая статья в твоём любимом разделе!'
                send_mail(subject, subject_message, 'subscription@newsagg.com', [user.email], html_message=html_message)