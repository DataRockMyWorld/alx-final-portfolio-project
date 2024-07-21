from django import forms
from .models import WorkCompletionForm, ToolboxTalkForm

class WorkCompletionFormForm(forms.ModelForm):
    class Meta:
        model = WorkCompletionForm
        fields = [
            'omc', 'time_commenced', 'time_completed', 'duration', 'material_used', 'quantity',
            'number_of_workmen', 'hours_worked', 'kilometers_traveled', 'lost_time_incidents',
            'medical_treatment_cases', 'first_aid_cases', 'oil_spilled', 'fire_incident', 'site_comment', 'image'
        ]
        
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class ToolboxTalkFormForm(forms.ModelForm):
    class Meta:
        model = ToolboxTalkForm
        fields = [
            'omc', 'site_name', 'Job_description', 'attendees', 'image', 'toolbox_talk',
        ]
