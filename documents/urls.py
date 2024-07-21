from django.urls import path
from .views import upload_document, document_list, document_categories, document_category_list, document_delete

urlpatterns = [
    path('categories/', document_categories, name='document_categories'),
    path('upload/', upload_document, name='upload_document'),
    path('list/', document_list, name='document_list'),
    path('categories/<str:category>/', document_category_list, name='document_category_list'),
    path('delete/<int:document_id>/', document_delete, name='document_delete'),
]
