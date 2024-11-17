from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from .models import Document

@permission_required('bookshelf.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'bookshelf/document_list.html', {'documents': documents})

@permission_required('bookshelf.can_create', raise_exception=True)
def document_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Document.objects.create(title=title, content=content)
        return redirect('document_list')
    return render(request, 'bookshelf/document_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        document.title = request.POST.get('title')
        document.content = request.POST.get('content')
        document.save()
        return redirect('document_list')
    return render(request, 'bookshelf/document_form.html', {'document': document})

@permission_required('bookshelf.can_delete', raise_exception=True)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        document.delete()
        return redirect('document_list')
    return render(request, 'bookshelf/document_confirm_delete.html', {'document': document})

