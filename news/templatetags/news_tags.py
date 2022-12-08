from django import template
from django.db.models import *
from news.models import *

register = template.Library()

@register.simple_tag(name='get_cat')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt = Count('news', filter=F('news__is_published'))).filter(cnt__gt = 1)
    return {'categories': categories}
