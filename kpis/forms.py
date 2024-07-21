from django import forms
from .models import KPI

    
class DateForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class KPIFilterForm(forms.Form):
    objective = forms.ChoiceField(
        choices=[('','All')] + KPI.OBJECTIVES,
        required=False
    )
    category = forms.ChoiceField(
        choices=[('','All')] + KPI.CATEGORY_CHOICES,
        required=False
    )