from django.db import models

class Stylist(models.Model):
    """
    A model representing a stylist.

    Fields:
    - name (CharField): The name of the stylist.
    - specialty (CharField): The specialty of the stylist.
    - created_at (DateTimeField): The datetime when the stylist was created.
    - updated_at (DateTimeField): The datetime when the stylist was last updated.
    """
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Service(models.Model):
    """
    A model representing a service.

    Fields:
    - name (CharField): The name of the service.
    - price (DecimalField): The price of the service.
    - duration (DurationField): The duration of the service.
    - created_at (DateTimeField): The datetime when the service was created.
    - updated_at (DateTimeField): The datetime when the service was last updated.
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appointment(models.Model):
    """
    A model representing an appointment.

    Fields:
    - stylist (ForeignKey): The stylist associated with the appointment.
    - service (ForeignKey): The service associated with the appointment.
    - customer_name (CharField): The name of the customer for the appointment.
    - discount (FloatField): The discount applied to the appointment.
    - appointment_date (DateTimeField): The datetime of the appointment.
    - created_at (DateTimeField): The datetime when the appointment was created.
    - updated_at (DateTimeField): The datetime when the appointment was last updated.
    """
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    discount = models.FloatField(default=0)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
