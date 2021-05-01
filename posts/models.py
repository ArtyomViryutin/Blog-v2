from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    text = models.TextField('Текст', help_text='Введите содержимое поста')
    pub_date = models.DateTimeField('Дата публикации поста', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name='Изображение',
                              help_text='Загрузите изображение')

    def __str__(self):
        return self.text[:15]

    def get_absolute_url(self):
        return reverse('post', kwargs={'username': self.author.username, 'pk': self.id})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    text = models.TextField('Комментарий', help_text='Введите текст коммпентария')
    created = models.DateTimeField('Дата публикации комментария', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')

    def __str__(self):
        return self.text[:15]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', verbose_name='Автор')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', verbose_name='Подписчик')
    follow_date = models.DateTimeField('Дата начала подписки', auto_now_add=True)

    def __str__(self):
        return self.author.__str__() + ' - ' + self.user.__str__()

    class Meta:
        verbose_name = 'Подсписка'
        verbose_name_plural = 'Подписки'


class Viewing(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='viewings', verbose_name='Пост')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viewings', verbose_name='Пользователь')
    view_date = models.DateTimeField('Дата просмотра поста', auto_now_add=True)

    def __str__(self):
        return self.post.__str__() + ' ' + self.user.__str__()

    class Meta:
        verbose_name = 'Просмотр'
        verbose_name_plural = 'Просмотры'
