# The list of commands

 python manage.py shell

## 1. Создать двух пользователей (с помощью метода User.objects.create_user).
	from django.contrib.auth.models import User
	from news.models import Author, Category, Post, Comment, PostCategory

## 2. Создать два объекта модели Author, связанные с пользователями.
	user1 = User.objects.create_user(username='user1', password='1234')
	author1 = Author.objects.create(user=user1)
	user2 = User.objects.create_user(username='user2', password='1234')
	author2 = Author.objects.create(user=user2)

## 3. Добавить 4 категории в модель Category.
	main_category_names = ["Sport", "Politics", "Technology", "Health"]
	for category_name in main_category_names:
		category, created = Category.objects.get_or_create(name=category_name)

## 4. Добавить 2 статьи и 1 новость.
article1 = Post.objects.create(author=author1,
news_type=Post.article, title='Секреты успешного спортсмена', content='Статья о том, как стать успешным спортсменом и достичь вершин в любом виде спорта...',
)
article2 = Post.objects.create(author=author2,
news_type=Post.article, title='Глобальные политические кризисы 2023 года', content='Обзор наиболее влиятельных политических событий в мире за 2023 год...',
)
news1 = Post.objects.create(author=author1,
news_type=Post.article, title='Новейшие технологии в образовании', content='Новость о внедрении новых технологий в образовательные учреждения...',
)

## 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
sport_category = Category.objects.get(name='Sport')
health_category = Category.objects.get(name='Health')
politic_category = Category.objects.get(name='Politic')
technology_category = Category.objects.get(name='Technology')

article1.categories.add(sport_category, health_category)
article2.categories.add(politic_category, health_category)
news1.categories.add(politic_category, technology_category)

## 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comment1_article1 = Comment.objects.create(post=article1, user=author2.user, content='Отличная статья!',
)
comment2_article1 = Comment.objects.create(post=article1, user=author1.user, content='Дерьмовая статья!',
)
comment1_article2 = Comment.objects.create(post=article2, user=author1.user, content='Спасибо за инфу!',
)
comment1_news1 = Comment.objects.create(post=news1, user=author2.user, content='Захватывающе!',
)

## 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
article1.like()
article1.save()

article2.dislike()
article2.save()

news1.like()
news1.save()

comment1_article1.like() 
comment1_article1.save()

comment2_article1.dislike()
comment2_article1.save()

comment1_article2.like()
comment1_article2.save()

comment1_news1.like()
comment1_news1.save()

## 8. Обновить рейтинги пользователей.
authors = Author.objects.all()
for author in authors: author.update_rating() author.save()

## 9.  Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
best_author = Author.objects.all().order_by('-rating').first()
if best_author:
	user = best_author.user
	rating = best_author.rating
	print(f"User: {user}")
	print(f"Rating: {rating}")
else:
	print("No authors found.")

## 10.  Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
best_article = Post.objects.filter(news_type=Post.article).order_by('-rating').first()
if best_article:
	author = best_article.author.user.username
	created_at = best_article.created_at
	rating = best_article.rating
	title = best_article.title
	preview = best_article.preview()

	print(f"Date of Addition: {created_at}")
	print(f"Author Username: {author}")
	print(f"Rating: {rating}")
	print(f"Title: {title}")
	print(f"Preview: {preview}")
else:
	print("No articles found.")

## 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
for comment in comments_for_best_article:
	comment_date = comment.created_at
	comment_user = comment.user.username
	comment_rating = comment.rating
	comment_text = comment.content

	print(f"Date: {comment_date}")
	print(f"User: {comment_user}")
	print(f"Rating: {comment_rating}")
	print(f"Text: {comment_text}")
	print()