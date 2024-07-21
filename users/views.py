from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from forms.models import WorkCompletionForm, ToolboxTalkForm
from incidents.models import IncidentReport
from documents.models import Document
from .forms import UserRegistrationForm, ProfilePictureForm
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User
from django.db.models import Count
from django.db.models.functions import TruncMonth
from itertools import chain

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user =form.save()
            # Send email notification to HSSE Manager
            subject = 'New User Registration - Approval Required'
            message = f'A new user has registered:\n\nUsername: {user.username}\nEmail: {user.email}\nDepartment: {user.department}\n\nPlease log in to the admin panel to approve this user.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['jewel.bansah@gpsghana.org']  # Update with actual HSSE Manager's email
            send_mail(subject, message, from_email, recipient_list)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')

@login_required
def account(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = ProfilePictureForm(instance=request.user)

    return render(request, 'users/account.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_manager)
def approve_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.is_approved = True
        user.save()
        return redirect('user_list')
    return render(request, 'users/approve_user.html', {'user': user})

@login_required
@user_passes_test(lambda u: u.is_manager)
def user_list(request):
    users = User.objects.filter(is_approved=False)
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def dashboard(request):
    work_completion_count = WorkCompletionForm.objects.filter(user=request.user).count()
    incident_report_count = IncidentReport.objects.filter(user=request.user).count()
    toolbox_talk_count = ToolboxTalkForm.objects.filter(user=request.user).count()

    work_completion_data = WorkCompletionForm.objects.filter(user=request.user).annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id'))
    incident_report_data = IncidentReport.objects.filter(user=request.user).annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id'))
    toolbox_talk_data = ToolboxTalkForm.objects.filter(user=request.user).annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id'))

    # Combine the data from all forms
    combined_data = list(chain(work_completion_data, incident_report_data, toolbox_talk_data))
    
    # Sort combined data by month
    combined_data = sorted(combined_data, key=lambda x: x['month'])

    form_counts = {
        'work_completion': work_completion_count,
        'incident_report': incident_report_count,
        'toolbox_talk': toolbox_talk_count,
    }

    total_forms_filled = work_completion_count + incident_report_count + toolbox_talk_count

    context = {
        'form_counts': form_counts,
        'forms_filled_over_time': combined_data,
        'total_forms_filled': total_forms_filled
    }

    return render(request, 'users/dashboard.html', context)