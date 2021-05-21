from django.db import models

class CommonInfo(models.Model):
    Name = models.CharField(max_length=50)
    Mobile_No = models.CharField(max_length=10)
    Code = models.CharField(unique=True, max_length=15)
    Location = models.CharField(max_length=50)
    class Meta:
        abstract = True

class DoctorDetail(CommonInfo):
    pass

class PatientDetail(CommonInfo):
      Code = None
    
class MedicienDetail(CommonInfo):
    Company_Name = models.CharField(max_length=50)
    Mobile_No = None
    Location = None
