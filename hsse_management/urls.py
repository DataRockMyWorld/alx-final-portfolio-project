"""
URL configuration for hsse_management project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("forms/", include("forms.urls")),
    path('incidents/', include('incidents.urls')),
    path('documents/', include('documents.urls')),
    path('kpis/', include('kpis.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
