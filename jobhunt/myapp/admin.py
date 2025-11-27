from django.contrib import admin
from .models import City, Company, Type, Platform, Status, Job, Application, Interview

# Register your models here.
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Type)
admin.site.register(Platform)
admin.site.register(Status)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Interview)
