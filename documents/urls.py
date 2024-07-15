from django.urls import path
from .views import upload_document, document_list, document_categories

urlpatterns = [
    path('categories/', document_categories, name='document_categories'),
    path('upload/', upload_document, name='upload_document'),
    path('list/', document_list, name='document_list'),
]
