from django.urls import path
from .views import incident_report_form, incident_report_list

urlpatterns = [
    path('incident_report/', incident_report_form, name='incident_report_form'),
    path('incident_report/list/', incident_report_list, name='incident_report_list'),
]
