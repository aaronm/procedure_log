from django.contrib import admin
from .models import Trainee, Attending, Procedure, Procedure_Code, Patient, Procedure_Map

admin.site.register(Attending)
#admin.site.register(Procedure)
admin.site.register(Procedure_Code)
admin.site.register(Patient)
admin.site.register(Procedure_Map)

# Register your models here.
class ProcedureInline(admin.StackedInline):
    model = Procedure
    
    
class TraineeAdmin(admin.ModelAdmin):

    inlines = [ProcedureInline]

class ProcedureCodeInline(admin.StackedInline):
	model = Procedure_Code
	extra = 0

	
class ProcedureAdmin(admin.ModelAdmin):
	
	inlines = [ProcedureCodeInline]

admin.site.register(Trainee, TraineeAdmin)
admin.site.register(Procedure, ProcedureAdmin)