from django.urls import path
from .views import TaggedPostListView, register, user_login, user_logout, profile, PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView,PostByTagListView, search

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

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    path('search/', search, name='search'),
    path('tags/<str:tag_name>/', TaggedPostListView.as_view(), name='tagged_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name="posts_by_tag"),
]