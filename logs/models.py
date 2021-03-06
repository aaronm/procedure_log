from django.db import models
from itertools import chain

# Create your models here.
class Attending(models.Model):
	full_name = models.CharField(max_length=100, null=True, blank=True)
	abbrev_name = models.CharField(max_length=50)

	def __str__(self):              # __unicode__ on Python 2
		return self.abbrev_name

class Trainee(models.Model):
	full_name = models.CharField(max_length=100, null=True, blank=True)
	abbrev_name = models.CharField(max_length=50)

	def __str__(self):              # __unicode__ on Python 2
		return self.abbrev_name
    
class Procedure(models.Model):
	description = models.CharField(max_length=200, default = '')
	fluoro_time = models.IntegerField(default=0, null=True, blank=True)
	start_time = models.DateTimeField(null=True, blank=True)
	duration = models.DurationField(null=True, blank=True)
	attending = models.ForeignKey(Attending, null=True, blank=True)
	trainee = models.ForeignKey(Trainee, null=True, blank=True)
	mrn = models.CharField(max_length=30, default = '')
	tech = models.CharField(max_length=20, default = '')
	location = models.CharField(max_length=10, default = '')
	inpatient = models.IntegerField(default = 0)
	outpatient = models.IntegerField(default = 1)
	
	def __str__(self):
		if self.description:
			return self.description
			print "returned a description"
		all_desc = ""
		print self.procedure_code_set.values()
		codes = self.procedure_code_set.values('code')
		print chain(*codes)
		code_maps = Procedure_Map.objects.all()
		code_list = ''
		#code_list = codes.values()
		for code_map in code_maps:
			proc_codes = code_map.codes.replace(".",",")
			codearray = proc_codes.split(",")
			if set(codearray) == set(code_list):
				#self.description = code_map.abbrev_name
				#self.save()
				return code_map.abbrev_name
		descriptions = self.procedure_code_set.values('description')
		for description in descriptions:
			all_desc +=  description['description'] +";"
		return all_desc
		
		
    
class Procedure_Code(models.Model):
	code = models.CharField(max_length=50, default ='')
	description = models.CharField(max_length=200, default = '')
	procedure = models.ForeignKey(Procedure, null=True, blank=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.description
    
class Patient(models.Model):
    mrn = models.CharField(max_length=30, default = '')
    
class Procedure_Map(models.Model):
	codes = models.CharField(max_length=200, default='0')
	full_name = models.CharField(max_length=100, default='')
	abbrev_name = models.CharField(max_length=50, default='')
