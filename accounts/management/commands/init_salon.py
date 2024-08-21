from django.core.management.base import BaseCommand
from django.core.management import call_command
from accounts.models import Salon
from django.conf import settings

class Command(BaseCommand):
    """
    Management command to initialize databases for all salons and apply migrations
    """
    help = 'Initialize databases for all salons and apply migrations'

    def handle(self, *args, **kwargs):
        for salon in Salon.objects.all():
            db_name = f'{salon.db_name}_db'
            if db_name in settings.DATABASES:
                # Apply all migrations for the new database
                try:
                    call_command('migrate', database=db_name, app_label='salon', verbosity=0)
                    self.stdout.write(self.style.SUCCESS(f'Successfully applied migrations for database: {db_name}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error applying migrations for database {db_name}: {e}'))
            else:
                self.stdout.write(self.style.ERROR(f'Database connection {db_name} not found'))
