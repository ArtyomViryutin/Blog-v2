from django import template

from posts.models import Follow, Viewing

register = template.Library()


@register.simple_tag
def is_subscribed(user, author):
    return Follow.objects.filter(author=author, user=user).exists()


@register.simple_tag
def is_viewed(user, post):
    if user.is_authenticated:
        return Viewing.objects.filter(post=post, user=user).exists()
    return False
