from django.db import models

# Create your models here.


class Specie(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Animal(models.Model):
    name = models.CharField(max_length=100)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class WeightEntry(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()

    class Meta:
        unique_together = ('animal', 'date')

    def __str__(self):
        return f"{self.animal.name} - {self.date}: {self.weight}kg"


class Appointment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.animal.name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"


class Medicine(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date_prescribed = models.DateField(auto_now_add=True)
    dosage = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.medicine.name} for {self.animal.name} - {self.date_prescribed}"
