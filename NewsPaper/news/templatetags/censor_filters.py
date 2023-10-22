from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    
    unwanted_words = ["черт", "дурак", "Налоговая"]

    # Заменяем нежелательные слова на символы "*"
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))

    return value