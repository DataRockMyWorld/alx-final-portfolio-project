from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .forms import DocumentForm
from .models import Document


def is_hsse_manager(user):
    return user.is_manager

@login_required
@user_passes_test(is_hsse_manager)
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/upload_document.html', {'form': form})

@login_required
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})

@login_required
def document_categories(request):
    return render(request, 'documents/document_categories.html')

def document_category_list(request, category):
    documents = Document.objects.filter(category=category)
    return render(request, 'documents/document_list.html', {'documents': documents, 'category': category})

@login_required
def document_delete(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('document_category_list', category=document.category)
    return render(request, 'documents/document_confirm_delete.html', {'document': document})
