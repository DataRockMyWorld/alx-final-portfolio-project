from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import IncidentReportForm
from .models import IncidentReport
from django.contrib import messages

@login_required
def incident_report_form(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            incident_form = form.save(commit=False)
            incident_form.user = request.user
            incident_form.save()
            messages.success(request, 'Form successfully submitted!')
            return redirect('dashboard')
    else:
        form = IncidentReportForm()
    return render(request, 'incidents/incident_report_form.html', {'form': form})

@login_required
def incident_report_list(request):
    forms = IncidentReport.objects.filter(user=request.user)
    return render(request, 'incidents/incident_report_list.html', {'forms': forms})
