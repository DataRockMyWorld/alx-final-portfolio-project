from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.kpi_dashboard, name='kpi_dashboard'),
    path('export/csv/', views.export_kpi_csv, name='export_kpi_csv'),
    path('export/pdf/', views.export_kpi_pdf, name='export_kpi_pdf'),
]
