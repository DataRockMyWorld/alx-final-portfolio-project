from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from forms.models import WorkCompletionForm
from incidents.models import IncidentReport
from documents.models import Document
from .forms import UserRegistrationForm, UserProfileForm
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User

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
    user_forms = WorkCompletionForm.objects.filter(user=request.user)
    user_incidents = IncidentReport.objects.filter(user=request.user)
    user_documents = Document.objects.filter(uploaded_by=request.user)
    return render(request, 'users/dashboard.html', {
        'user_forms': user_forms,
        'user_incidents': user_incidents,
        'user_documents': user_documents,
    })

@login_required
def account(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/account.html', {'form': form})
