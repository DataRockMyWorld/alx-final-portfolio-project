from django import forms
from .models import IncidentReport

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = [
            'site', 'date', 'time', 'incident_type', 'impact_type', 'details', 'location',
            'immediate_action', 'status', 'incident_number'
        ]
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
