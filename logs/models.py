from django.db import models

# Create your models here.
class Attending(models.Model):
    full_name = models.CharField(max_length=100)
    abbrev_name = models.CharField(max_length=50)

class Trainee(models.Model):
    full_name = models.CharField(max_length=100)
    abbrev_name = models.CharField(max_length=50)
    
class Procedure(models.Model):
    description = models.CharField(max_length=200)
    fluoro_time = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    attending = models.ForeignKey(Attending)
    trainee = models.ForeignKey(Trainee)
    
class Procedure_Code(models.Model):
    code = models.IntegerField(default =0)
    description = models.CharField(max_length=200)
    procedure = models.ForeignKey(Procedure)
    location = models.CharField(max_length=10)
    inpatient = models.IntegerField(default = 0)
    outpatient = models.IntegerField(default = 1)
    
class Patient(models.Model):
    mrn = models.CharField(max_length=30)
    