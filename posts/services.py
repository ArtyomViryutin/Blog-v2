from django.core.mail import send_mass_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_mails(to_emails, template):
    # html_message = render_to_string(template_name=template, context={'author': author})
    # plain_message = strip_tags(html_message)
    subscribers_emails = []
