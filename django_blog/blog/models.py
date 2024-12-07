from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    User = get_user_model()
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self):
        return f"{self.title} by {self.author} in {self.published_date}"
