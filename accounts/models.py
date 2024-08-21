from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext as _
from django.db import models
import logging
from django.db import connections, OperationalError
from django.core.management import call_command
from django.conf import settings
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

logger = logging.getLogger(__name__)



class CustomUserManager(BaseUserManager):
    """Custom user manager for managing user creation."""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        return queryset



class User(AbstractBaseUser, PermissionsMixin):
    """User model representing a user in the system."""

    name = models.CharField(max_length=255)
    phone = models.CharField(_("phone number"), max_length=20)
    email = models.EmailField(_("email"), max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)
    
    
    USERNAME_FIELD = "email"
    
    
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.name



class Salon(models.Model):
    
    """Salon model representing a salon in the system."""

    name = models.CharField(max_length=255)
    db_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        create_database(self.db_name)
        
        

def create_database(db_name):
    """Function to create a new database based on the provided name."""

    db_name = f'{db_name}_db'

    # Establish a connection to the default PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.environ.get('DATABASE_NAME'),
        user=os.environ.get('DATABASE_USER_NAME'),
        password=os.environ.get('DATABASE_PASSWORD'),
        host=os.environ.get('DATABASE_HOST'),
        port=os.environ.get('DATABASE_PORT')
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Create the new database if it does not exist
    cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(f'CREATE DATABASE {db_name}')
    
    cursor.close()
    conn.close()
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
        'OPTIONS': {},
        'AUTOCOMMIT': True,
        'ATOMIC_REQUESTS': False, 
    }
    connection = connections[db_name]
    try:
        connection.ensure_connection()
        call_command('migrate', database=db_name, app_label='salon', verbosity=0)
    except OperationalError:
        pass