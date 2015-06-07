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
    extra = 10
    
    
class TraineeAdmin(admin.ModelAdmin):

    inlines = [ProcedureInline]
    class Media:
        js = ['js/jquery-1.3.2.min.js', 'static/js/collapsed_stacked_inlines.js',]

admin.site.register(Trainee, TraineeAdmin)