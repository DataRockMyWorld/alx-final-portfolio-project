from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkCompletionFormForm, ToolboxTalkFormForm
from .models import WorkCompletionForm, ToolboxTalkForm
from django.contrib import messages

@login_required
def work_completion_form(request):
    if request.method == 'POST':
        form = WorkCompletionFormForm(request.POST)
        if form.is_valid():
            work_form = form.save(commit=False)
            work_form.user = request.user
            work_form.save()
            messages.success(request, 'Work Completion Form successfully submitted!')
            return redirect('work_completion_form')
    else:
        form = WorkCompletionFormForm()
    return render(request, 'forms/work_completion_form.html', {'form': form})

@login_required
def work_completion_list(request):
    forms = WorkCompletionForm.objects.filter(user=request.user)
    return render(request, 'forms/work_completion_list.html', {'forms': forms})

@login_required
def toolbox_talk_form(request):
    if request.method == 'POST':
        form = ToolboxTalkFormForm(request.POST)
        if form.is_valid():
            toolbox_form = form.save(commit=False)
            toolbox_form.user = request.user
            toolbox_form.save()
            messages.success(request, 'Toolbox Talk Form successfully submitted!')
            return redirect('toolbox_talk_form')
    else:
        form = ToolboxTalkFormForm()
    return render(request, 'forms/toolbox_talk_form.html', {'form': form})

@login_required
def toolbox_talk_list(request):
    forms = ToolboxTalkForm.objects.filter(user=request.user)
    return render(request, 'forms/toolbox_talk_list.html', {'forms': forms})

@login_required
def form_list(request):
    return render(request, 'forms/form_list.html')
