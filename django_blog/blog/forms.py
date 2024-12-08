from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class PostForm(forms.ModelForm):
    class Meta:
        models = Post
        fields = ['title', 'content']
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Blog Post Title"
        self.fields['content'].label = "Blog Post Content"
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']