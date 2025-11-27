from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application, Interview, Type, Platform, Company
from .forms import ApplicationForm, JobForm, CompanyForm, InterviewForm

def dashboard(request):
    from django.utils import timezone
    jobs = Job.objects.all()
    applications = Application.objects.all()
    interviews = Interview.objects.filter(date__gte=timezone.now().date())
    context = {
        'jobs': jobs,
        'applications': applications,
        'interviews': interviews,
        'total_jobs': jobs.count(),
        'total_applications': applications.count(),
        'total_interviews': interviews.count(),
    }
    return render(request, 'myapp/dashboard.html', context)

def interviews_list(request):
    interviews = Interview.objects.all().order_by('-date')
    context = {
        'interviews': interviews,
    }
    return render(request, 'myapp/interviews_list.html', context)

def interview_detail(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    context = {
        'interview': interview,
    }
    return render(request, 'myapp/interview_detail.html', context)

def applications_list(request):
    applications = Application.objects.all().order_by('-date')
    context = {
        'applications': applications,
    }
    return render(request, 'myapp/applications_list.html', context)

def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    context = {
        'application': application,
    }
    return render(request, 'myapp/application_detail.html', context)

def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applications_list')
    else:
        initial = {}
        job_pk = request.GET.get('job')
        if job_pk:
            try:
                job = Job.objects.get(pk=job_pk)
                initial['job'] = job
            except Job.DoesNotExist:
                pass
        form = ApplicationForm(initial=initial)
    context = {
        'form': form,
    }
    return render(request, 'myapp/add_application.html', context)

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            return redirect(f'/applications/add/?job={job.pk}')
    else:
        form = JobForm()
    context = {
        'form': form,
    }
    return render(request, 'myapp/add_job.html', context)

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CompanyForm()
    context = {
        'form': form,
    }
    return render(request, 'myapp/add_company.html', context)

def add_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interviews_list')
    else:
        initial = {}
        app_pk = request.GET.get('application')
        if app_pk:
            try:
                application = Application.objects.get(pk=app_pk)
                initial['application'] = application
            except Application.DoesNotExist:
                pass
        form = InterviewForm(initial=initial)
    context = {
        'form': form,
    }
    return render(request, 'myapp/add_interview.html', context)

def stats(request):
    from django.db.models import Count
    types_stats = []
    for type_obj in Type.objects.all():
        applications = Application.objects.filter(type=type_obj)
        answered = applications.filter(is_answered=True).count()
        interviews = Interview.objects.filter(application__type=type_obj).count()
        types_stats.append({
            'type': type_obj.name,
            'total_applications': applications.count(),
            'answered': answered,
            'interviews': interviews,
            'answer_rate': answered / applications.count() * 100 if applications.count() > 0 else 0,
            'interview_rate': interviews / applications.count() * 100 if applications.count() > 0 else 0,
        })

    platforms_stats = []
    for platform in Platform.objects.exclude(name="Company's website"):
        applications = Application.objects.filter(platform=platform)
        answered = applications.filter(is_answered=True).count()
        interviews = Interview.objects.filter(application__platform=platform).count()
        platforms_stats.append({
            'platform': platform.name,
            'total_applications': applications.count(),
            'answered': answered,
            'interviews': interviews,
            'answer_rate': answered / applications.count() * 100 if applications.count() > 0 else 0,
            'interview_rate': interviews / applications.count() * 100 if applications.count() > 0 else 0,
        })

    context = {
        'types_stats': types_stats,
        'platforms_stats': platforms_stats,
    }
    return render(request, 'myapp/stats.html', context)
