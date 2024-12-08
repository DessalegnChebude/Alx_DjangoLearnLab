from django.urls import path
from .views import register, user_login, user_logout, profile, PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/comments/<int:comment_id>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_id>/comments/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]