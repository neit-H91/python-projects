from django import forms
from .models import Application, Job, Company, Interview

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['date', 'type', 'job', 'platform', 'status', 'is_answered']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'post_link', 'resume']
        widgets = {
            'resume': forms.Textarea(attrs={'rows': 4}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'city']

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['date', 'application', 'notes']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
