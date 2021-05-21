from django.contrib import admin
from .models import DoctorDetail,PatientDetail,MedicienDetail

@admin.register(DoctorDetail)
class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Code','Mobile_No','Location']

@admin.register(PatientDetail)
class PatientDetailsAdmin(admin.ModelAdmin):
    list_display =['id', 'Name','Mobile_No','Location']

@admin.register(MedicienDetail)
class MedicienDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name','Code','Company_Name']