from django.http import HttpResponse
from django.shortcuts import render
import csv
from .models import KPI
from forms.models import WorkCompletionForm, ToolboxTalkForm
from incidents.models import IncidentReport
from django.template.loader import render_to_string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.db.models.functions import TruncMonth
from django.db.models import Sum, Count, Avg
from django.contrib.auth.decorators import login_required
from .forms import DateForm, KPIFilterForm
from django.core.paginator import Paginator


def export_kpi_pdf(request):
    kpis = KPI.objects.all()
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.drawString(100, height - 100, "KPI Report")
    p.line(100, height - 105, width - 100, height - 105)

    y = height - 120
    p.drawString(100, y, "Name")
    p.drawString(200, y, "Category")
    p.drawString(300, y, "Target Value")
    p.drawString(400, y, "Actual Value")
    p.drawString(500, y, "Percentage Achieved")
    p.line(100, y - 5, width - 100, y - 5)

    for kpi in kpis:
        y -= 20
        p.drawString(100, y, kpi.kpi_name)
        p.drawString(200, y, kpi.category)
        p.drawString(300, y, str(kpi.target_value))
        p.drawString(400, y, str(kpi.actual_value))
        p.drawString(500, y, f"{kpi.percentage_achieved()}%")

    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


@login_required
def kpi_dashboard(request):
    kpis = KPI.objects.all()
    date_form = DateForm(request.GET or None)
    filter_form = KPIFilterForm(request.GET or None)
    kpi_data = []

    if date_form.is_valid():
        selected_date = date_form.cleaned_data['date']
        work_completion_forms = WorkCompletionForm.objects.filter(date=selected_date)
        incident_reports = IncidentReport.objects.filter(date=selected_date)
        toolbox_talk_forms = ToolboxTalkForm.objects.filter(date=selected_date)
    else:
        work_completion_forms = WorkCompletionForm.objects.all()
        incident_reports = IncidentReport.objects.all()
        toolbox_talk_forms = ToolboxTalkForm.objects.all()

    for kpi in kpis:
        actual_value = 0
        if kpi.kpi_name == 'oil_spilled':
            actual_value = work_completion_forms.count()
        elif kpi.kpi_name == 'incident_number':
            actual_value = incident_reports.count()
        elif kpi.kpi_name == 'toolbox_talk':
            actual_value = toolbox_talk_forms.count()
        elif kpi.kpi_name == 'first_aid_cases':
            actual_value = work_completion_forms.count()
        
        kpi_data.append({
            'objective': kpi.Objective,
            'kpi_name': kpi.kpi_name,
            'category': kpi.category,
            'target_value': kpi.target_value,
            'actual_value': actual_value,
            'percentage_achieved': kpi.percentage_achieved(actual_value),
        })

    # Filtering
    if filter_form.is_valid():
        objective = filter_form.cleaned_data.get('objective')
        category = filter_form.cleaned_data.get('category')
        if objective:
            kpis = kpis.filter(Objective=objective)
        if category:
            kpis = kpis.filter(category=category)

    # Pagination
    paginator = Paginator(kpi_data, 10)  # Show 10 KPIs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    kpi_categories = kpis.values('category').annotate(total=Sum('target_value'))
    kpi_trends = []  # Populate this with appropriate data if needed

    context = {
        'date_form': date_form,
        'filter_form': filter_form,
        'kpis': page_obj,
        'kpi_categories': list(kpi_categories),
        'kpi_trends': list(kpi_trends),
    }

    return render(request, 'kpis/kpi_dashboard.html', context)

def export_kpi_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kpis.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'Target Value', 'Actual Value', 'Percentage Achieved'])

    kpis = KPI.objects.all()
    for kpi in kpis:
        writer.writerow([kpi.kpi_name, kpi.category, kpi.target_value, kpi.actual_value, kpi.percentage_achieved()])

    return response
