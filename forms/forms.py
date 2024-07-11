from django import forms
from .models import WorkCompletionForm, ToolboxTalkForm

class WorkCompletionFormForm(forms.ModelForm):
    class Meta:
        model = WorkCompletionForm
        fields = [
            'omc', 'time_commenced', 'time_completed', 'material_used', 'quantity',
            'number_of_workmen', 'hours_worked', 'kilometers_traveled',
            'lost_time_incidents', 'medical_treatment_cases', 'first_aid_cases',
            'oil_spilled', 'site_comment', 'google_address'
        ]

class ToolboxTalkFormForm(forms.ModelForm):
    class Meta:
        model = ToolboxTalkForm
        fields = ['talk_date', 'subject', 'details', 'attendees', 'location', 'image']
