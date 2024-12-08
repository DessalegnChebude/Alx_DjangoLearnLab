from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        self.name
        
class Post(models.Model):
    # User = get_user_model()
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()
    
    def __str__(self):
        return f"{self.title} by {self.author} in {self.published_date}"

# Implement Profile Management
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"
    
