from django.contrib import admin
from .models import KPI

@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display = ('kpi_name', 'category', 'target_value', 'actual_value')
    list_filter = ('Objective', 'category')
    search_fields = ('kpi_name', 'category')
