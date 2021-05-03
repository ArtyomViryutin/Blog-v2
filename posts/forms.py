from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
