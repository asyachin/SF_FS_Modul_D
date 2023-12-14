from django.core.management.base import BaseCommand, CommandError, CommandParser
from news.models import Category, Post
import sys

class Command(BaseCommand):
		help = 'Deletes all news posts in a specified category'

		def add_arguments(self, parser):
			parser.add_argument('category', type=str, help='Name of teh categorry from which to delete news')
   
		def handle(self, *args, **options):
				category = options['category']
				try:
						category = Category.objects.get(name=category)
				except Category.DoesNotExist:
						self.stdout.write(self.style.ERROR(f'Category "{category}" does not exist'))
						sys.exit(1)

# Confirm deletion
				self.stdout.write(f'You are about to delete all news posts in the category: "{category}"')
				confirm = input("Are you sure you want to do this? Type 'yes' to continue: ")
				if confirm != 'yes':
						self.stdout.write(self.style.NOTICE('Deletion cancelled.'))
						sys.exit(0)

# Delete posts
				posts = Post.objects.filter(categories=category)
				count = posts.count()
				posts.delete()
				self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} news post(s) from category "{category}"'))