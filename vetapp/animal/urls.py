from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('<int:id>/', views.animal_detail, name='animal_detail'),
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/<int:id>/', views.owner_detail, name='owner_detail'),
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/<int:id>/', views.medicine_detail, name='medicine_detail'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:id>/', views.appointment_detail, name='appointment_detail'),
]