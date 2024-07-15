from django.http import HttpResponse
from django.shortcuts import render
from .models import KPI
from .forms import TimePeriodForm
from .utils import calculate_kpi_value
from django.template.loader import render_to_string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

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

def kpi_dashboard(request):
    kpis = KPI.objects.all()
    form = TimePeriodForm(request.GET or None)
    kpi_values = []

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        for kpi in kpis:
            kpi.actual_value = calculate_kpi_value(kpi.kpi_name, start_date, end_date)
            kpi_values.append(kpi)

    return render(request, 'kpis/kpi_dashboard.html', {
        'form': form,
        'kpis': kpi_values
    })

def export_kpi_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kpis.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'Target Value', 'Actual Value', 'Percentage Achieved'])

    kpis = KPI.objects.all()
    for kpi in kpis:
        writer.writerow([kpi.kpi_name, kpi.category, kpi.target_value, kpi.actual_value, kpi.percentage_achieved()])

    return response
