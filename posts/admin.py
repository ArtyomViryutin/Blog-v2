from django.contrib import admin
from .models import (Post, Comment, Follow, Viewing)
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'pub_date')
    list_filter = ('pub_date', 'author')
    search_fields = ('text',)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('author',),)
        }),
        (None, {
            'fields': (('text',),)
        }),
        (None, {
            'fields': (('image',), 'get_image')
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="150" height="150"')

    get_image.short_description = 'Изображение'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'created',)
    list_filter = ('author', 'created',)
    search_fields = ('text',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')
    list_filter = ('author', 'user', 'follow_date')


@admin.register(Viewing)
class ViewingAdmin(admin.ModelAdmin):
    list_display = ('user', 'post',)
    list_filter = ('user', 'post', 'view_date')
