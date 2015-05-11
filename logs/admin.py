from django.contrib import admin
from .models import Trainee, Attending, Procedure, Procedure_Code, Patient

admin.site.register(Trainee)
admin.site.register(Attending)
admin.site.register(Procedure)
admin.site.register(Procedure_Code)
admin.site.register(Patient)

# Register your models here.
