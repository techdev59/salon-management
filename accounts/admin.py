from django.contrib import admin

from .models import User, Salon
# Register your models here.


"""
This file contains the admin configurations for User and Salon models.
"""

admin.site.register(User)
admin.site.register(Salon)