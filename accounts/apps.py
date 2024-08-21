from django.apps import AppConfig
from django.conf import settings
import os
from django.db import connections, OperationalError
from django.core.management import call_command


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'


    # def ready(self):
    #     self.load_salon_databases()

    def load_salon_databases(self):
        """
        Load salon databases based on Salon model entries.
        """
        from .models import Salon
        
        salons = Salon.objects.all()
        for org in salons:
            db_name = f'{org.db_name}_db'
            settings.DATABASES[db_name] = {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': f'{db_name}',
                'USER': os.environ.get('DATABASE_USER_NAME'),
                'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
                'TIME_ZONE': settings.TIME_ZONE,
                'USE_TZ': settings.USE_TZ,
                'CONN_HEALTH_CHECKS': False,
                'CONN_MAX_AGE': 0,
                'OPTIONS': {},  # Include an empty dictionary for OPTIONS
                'AUTOCOMMIT': True,  # Ensure AUTOCOMMIT is set
                'ATOMIC_REQUESTS': False, 
            }
            connection = connections[db_name]
            try:
                connection.ensure_connection()
                call_command('migrate', database=db_name, app_label='salon', verbosity=0)
                call_command('init_salon')
                
            except OperationalError:
                pass
