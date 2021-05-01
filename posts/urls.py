from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='index'),
    path('follow/', views.FollowPostsListView.as_view(), name='follow'),
    path('new/', views.PostCreateView.as_view(), name='new_post'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('<str:username>/follow/', views.FollowCreateView.as_view(), name='profile_follow'),
    path('<str:username>/unfollow/', views.FollowDeleteView.as_view(), name='profile_unfollow'),
    path('<str:username>/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('<str:username>/<int:pk>/comment', views.CommentCreateView.as_view(), name='add_comment'),
    path('<str:username>/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
]
