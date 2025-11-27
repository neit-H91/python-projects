from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('interviews/', views.interviews_list, name='interviews_list'),
    path('interviews/<int:pk>/', views.interview_detail, name='interview_detail'),
    path('applications/', views.applications_list, name='applications_list'),
    path('applications/<int:pk>/', views.application_detail, name='application_detail'),
    path('applications/add/', views.add_application, name='add_application'),
    path('jobs/add/', views.add_job, name='add_job'),
    path('companies/add/', views.add_company, name='add_company'),
    path('interviews/add/', views.add_interview, name='add_interview'),
    path('stats/', views.stats, name='stats'),
]
