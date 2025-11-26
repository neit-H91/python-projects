import json
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Animal, Owner, Specie, WeightEntry, Appointment, Medicine, Prescription

@login_required
def dashboard(request):
    # Check user permissions
    user = request.user
    is_vet = user.is_superuser
    is_secretary = user.groups.filter(name='Secretaries').exists()

    # Total counts
    total_animals = Animal.objects.count()
    total_clients = Owner.objects.count()
    total_species = Specie.objects.count()
    total_appointments = Appointment.objects.count()
    total_prescriptions = Prescription.objects.count()
    total_weight_entries = WeightEntry.objects.count()

    # Latest animals (last 10 added)
    latest_animals = Animal.objects.order_by('-id')[:10]

    # Animals by specie (with counts)
    specie_counts = Animal.objects.values('specie__name').annotate(count=models.Count('id')).order_by('-count')
    # Upcoming appointments (next 5)
    now = timezone.now()
    upcoming_appointments = Appointment.objects.filter(date_time__gt=now).order_by('date_time')[:5]

    context = {
        'user': user,
        'is_vet': is_vet,
        'is_secretary': is_secretary,
        'total_animals': total_animals,
        'total_clients': total_clients,
        'total_species': total_species,
        'total_appointments': total_appointments,
        'total_prescriptions': total_prescriptions,
        'total_weight_entries': total_weight_entries,
        'latest_animals': latest_animals,
        'specie_counts': specie_counts,
        'upcoming_appointments': upcoming_appointments,
    }
    return render(request, 'animal/dashboard.html', context)

@login_required
def animal_detail(request, id):
    try:
        animal = Animal.objects.get(pk=id)
        # Get weight entries ordered by date for chart
        weight_entries = animal.weightentry_set.order_by('date')

        # Prepare data for Chart.js
        dates = [entry.date.strftime('%Y-%m-%d') for entry in weight_entries]
        weights = [float(entry.weight) for entry in weight_entries]

        context = {
            'animal': animal,
            'weight_entries': weight_entries,
            'dates_json': mark_safe(json.dumps(dates)),
            'weights_json': mark_safe(json.dumps(weights))
        }
        return render(request, 'animal/animal_detail.html', context)
    except Animal.DoesNotExist:
        return render(request, 'animal/animal_detail.html', {'error': 'cant find this animal'})

@login_required
def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal/animal_list.html', {'animals': animals})

@login_required
def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'animal/owner_list.html', {'owners': owners})

@login_required
def owner_detail(request, id):
    try:
        owner = Owner.objects.get(pk=id)
        owner_animals = owner.animal_set.all()
        owner_appointments = Appointment.objects.filter(owner=owner).select_related('animal').order_by('date_time')
        context = {
            'owner': owner,
            'owner_animals': owner_animals,
            'owner_appointments': owner_appointments,
        }
        return render(request, 'animal/owner_detail.html', context)
    except Owner.DoesNotExist:
        return render(request, 'animal/owner_detail.html', {'error': 'Owner not found'})

@login_required
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'animal/medicine_list.html', {'medicines': medicines})

@login_required
def medicine_detail(request, id):
    try:
        medicine = Medicine.objects.get(pk=id)
        prescriptions = Prescription.objects.filter(medicine=medicine).select_related('animal', 'animal__owner')
        context = {
            'medicine': medicine,
            'prescriptions': prescriptions,
        }
        return render(request, 'animal/medicine_detail.html', context)
    except Medicine.DoesNotExist:
        return render(request, 'animal/medicine_detail.html', {'error': 'Medicine not found'})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.select_related('animal', 'owner').order_by('date_time')
    return render(request, 'animal/appointment_list.html', {'appointments': appointments})

@login_required
def appointment_detail(request, id):
    try:
        appointment = Appointment.objects.select_related('animal', 'owner').get(pk=id)
        context = {
            'appointment': appointment,
        }
        return render(request, 'animal/appointment_detail.html', context)
    except Appointment.DoesNotExist:
        return render(request, 'animal/appointment_detail.html', {'error': 'Appointment not found'})
