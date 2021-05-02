from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Follow, Post
from django.conf import settings


def send_mails_to_followers(post_id):
    post = Post.objects.get(id=post_id)
    followers_emails = []
    for follow in Follow.objects.filter(author_id=post.author_id):
        followers_emails.append(follow.user.email)
    html_message = render_to_string(template_name='email.html', context={'post': post})
    plain_message = strip_tags(html_message)
    send_mail(subject='Blog: NEW POST', message=plain_message, from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=followers_emails, html_message=html_message)
