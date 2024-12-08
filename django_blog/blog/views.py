from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.views import View
from django.db.models import Q

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
        else:
            messages.error(request, 'Registration faild. please correct the errors below.')
    
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'blog/login.html')
        
def user_logout(request):
    logout(request)
    messages.success(request, 'you have logged out successfully.')
    return redirect('login')
            
@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST['email']
        user.save()
        messages.success(request, 'Profile updated successfully.')
    return render(request, 'blog/profile.html', {'user': user})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.post = post
            Comment.author = request.user
            Comment.save()
        
        return redirect('post-detail', pk=post_id)
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, id = comment_id)
        form = CommentForm(instance=comment)
        return render(request, 'blog/comment_update.html', {'form': form, 'comment': comment})
    
    def post(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail')
        
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
        def post(self, request, post_id, comment_id):
            comment = get_object_or_404(Comment, request, id=comment_id)
            comment.delete()
            return redirect('post-detail', pk=post_id)

        def test_func(self):
            comment = self.get_object()
            return self.request.user == comment.author
        

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
        Q(title_icontains=query) | 
        Q(content_icontains = query) | 
        Q(tags__name__icontains=query)
    ).distinct() # distinct used to avoid duplicate results from multiple tags
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(tags__name__iexact=tag_name)