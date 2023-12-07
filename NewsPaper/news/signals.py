from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Author, Post, SubscriberCategory
from django.core.mail import send_mail
from django.template.loader import render_to_string
import logging

#logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.get_or_create(user=instance)
        

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        #print(f"Отправка приветственного email пользователю {instance.username}") #test
        subject = 'Добро пожаловать в NewsPaper!'
        message = f'Здравствуй, {instance.username}. Мы рады приветствовать тебя в нашем приложении!'
        html_message = render_to_string('sign/welcome_email.html', {'user': instance})
        send_mail(subject, message,  'team@newspaper.com', [instance.email], html_message=html_message)

    
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
        send_mail(subject, message, 'team@newspaper.com', [user.email], html_message=html_message)
        
        
@receiver(post_save, sender=Post)
def send_new_post_notification(sender, instance, created, **kwargs):
    if created:
        print(f"Отправка уведомления о новой статье для статьи {instance.title}")
        print(instance.category.name)
