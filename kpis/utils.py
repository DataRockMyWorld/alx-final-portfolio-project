from forms.models import WorkCompletionForm, ToolboxTalkForm
from django.db.models import Sum
from datetime import datetime
from incidents.models import IncidentReport

def calculate_kpi_value(kpi_name, start_date, end_date):
    if kpi_name == "Work Hours":
        return WorkCompletionForm.objects.filter(date__range=(start_date, end_date)).aggregate(Sum('hours_worked'))['hours_worked__sum'] or 0
    elif kpi_name == "Incidents Reported":
        return IncidentReport.objects.filter(date__range=(start_date, end_date)).count()
    # Add other KPIs as needed
    return 0
