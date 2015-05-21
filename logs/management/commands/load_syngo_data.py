from django.core.management.base import BaseCommand, CommandError
from logs.models import Trainee, Attending, Procedure, Procedure_Code, Patient

class SyngoDataLoader(BaseCommand):
	help = 'loads syngo data from a comma delimited CSV generated by Syngo people'
	
	def add_arguments(self, parser):
		parser.add_argument('poll_id', nargs='+', type=int)

	def handle(self, *args, **options):
		self.stdout.write(help)