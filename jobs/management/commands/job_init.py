from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    print('JOBS Print')
    
    def handle(self, *args, **options):
        app_name = 'jobs'
        if app_name == 'jobs':
            from jobs import jobs
            jobs.Run()