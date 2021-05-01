from django.urls import reverse
from django.views.generic import (DetailView, ListView, CreateView, UpdateView)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (Post, Comment, Follow, Viewing)
from .forms import (PostForm, CommentForm)
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect

User = get_user_model()


class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'index.html'
    ordering = '-pub_date'
    paginate_by = 10


class FollowPostsListView(LoginRequiredMixin, ListView):
    template_name = 'follow.html'
    paginate_by = 10

    def get_queryset(self):
        authors = Follow.objects.filter(user=self.request.user).values_list('author_id')
        posts = Post.objects.filter(author__id__in=authors)
        return posts.order_by('-pub_date')


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'new.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'profile.html'
    ordering = '-pub_date'
    paginate_by = 10

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.kwargs.get('username'))
        return self.author.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(Post, author__username=self.kwargs['username'], id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created')
        is_subscribed = Follow.objects.filter(author=self.object.author, user=self.request.user)
        context['is_subscribed'] = is_subscribed
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    slug_field = 'author__username'
    slug_url_kwarg = 'username'
    query_pk_and_slug = True
    template_name = 'edit.html'


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.post = get_object_or_404(Post, author__username=self.kwargs.get('username'),
                                             id=self.kwargs.get('pk'))
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post', kwargs={'username': self.kwargs.get('username'), 'pk': self.kwargs.get('pk')})


class FollowCreateView(LoginRequiredMixin, View):
    def post(self, request, username):
        author = get_object_or_404(User, username=username)
        if author != request.user:
            Follow.objects.get_or_create(author=author, user=request.user)
        return redirect(request.POST.get('next', '/'), username=username)


class FollowDeleteView(LoginRequiredMixin, View):
    def post(self, request, username):
        author = get_object_or_404(User, username=username)
        follow = get_object_or_404(Follow, author=author, user=request.user)
        follow.delete()
        return redirect(request.POST.get('next', '/'), username=username)






