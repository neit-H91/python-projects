from django.contrib import admin
from .models import Animal, Owner, Specie, WeightEntry, Appointment, Medicine, Prescription

# Register Species
@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register Owners (Clients)
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')

# Register Animals
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'specie', 'owner', 'birth_date')
    search_fields = ('name', 'specie__name', 'owner__first_name', 'owner__last_name')
    list_filter = ('specie', 'owner')
    raw_id_fields = ('owner',)  # For better performance with large owner lists

# Register Weight Entries
@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'weight')
    search_fields = ('animal__name',)
    list_filter = ('date', 'animal__specie')
    ordering = ('-date',)
    date_hierarchy = 'date'

# Register Appointments
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('animal', 'owner', 'date_time', 'reason')
    search_fields = ('animal__name', 'owner__first_name', 'reason')
    list_filter = ('date_time', 'animal__specie')
    ordering = ('-date_time',)
    date_hierarchy = 'date_time'

# Register Medicines
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')
    list_filter = ('price',)

# Register Prescriptions
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('animal', 'medicine', 'date_prescribed', 'dosage')
    search_fields = ('animal__name', 'medicine__name', 'dosage')
    list_filter = ('date_prescribed', 'medicine')
    date_hierarchy = 'date_prescribed'
