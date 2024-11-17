from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from .models import Document

from django.http import HttpResponse

def my_view(request):
    response = HttpResponse('Hello, world!')
    response['Content-Security-Policy'] = "default-src 'self';"
    return response



@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    documents = Document.objects.all()
    return render(request, 'bookshelf/document_list.html', {'documents': documents})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Document.objects.create(title=title, content=content)
        return redirect('document_list')
    return render(request, 'bookshelf/document_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        document.title = request.POST.get('title')
        document.content = request.POST.get('content')
        document.save()
        return redirect('document_list')
    return render(request, 'bookshelf/document_form.html', {'document': document})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        document.delete()
        return redirect('document_list')
    return render(request, 'bookshelf/document_confirm_delete.html', {'document': document})

from django.shortcuts import render, redirect
from .forms import ExampleForm  # Ensure this import is present
from django.http import HttpResponse

# Example view for handling a form
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle the form data (e.g., save it to the database or process it)
            return HttpResponse('Form submitted successfully!')
        else:
            return render(request, 'bookshelf/form_example.html', {'form': form})
    else:
        form = ExampleForm()  # Initialize an empty form
    return render(request, 'bookshelf/form_example.html', {'form': form})

# bookshelf/views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

