from django.shortcuts import render, get_object_or_404, render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# libraries for user creation and authentication
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Set Up Role-Based Views
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['books'] = self.objects.books.all()
    return context

# creating user registration form views
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # login the user after registration is completed
            return redirect('home')
    else:
        form = UserCreationForm()
    return render (request, 'relationship_app/register.html', {'form': form})

    # Set Up Role-Based Views
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

    # Create the Role-Based Views
# relationship_app/views.py (continued)

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

