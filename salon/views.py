from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Stylist, Service, Appointment
from django.contrib.auth.decorators import login_required


class AppointmentView:
    """
    A view that handles appointments.

    Methods:
    - list_appointments(request, db_alias): List all appointments.
    - create_appointment(request, db_alias): Create a new appointment.
    - retrieve_appointment(request, db_alias, appointment_id): Retrieve a specific appointment.
    - update_appointment(request, db_alias, appointment_id): Update a specific appointment.
    - delete_appointment(request, db_alias, appointment_id): Delete a specific appointment.
    """
    
    @login_required
    def list_appointments(request, db_alias):
        """
        List all appointments.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.

        Returns:
        - JsonResponse: JSON response with list of appointments.
        """
        appointments = Appointment.objects.using(db_alias).all()
        data = [
            {
                "id": appointment.id,
                "stylist": appointment.stylist.name,
                "service": appointment.service.name,
                "customer_name": appointment.customer_name,
                "discount": appointment.discount,
                "appointment_date": appointment.appointment_date,
            } 
            for appointment in appointments
        ]
        return JsonResponse(data, safe=False)
    
    @login_required
    def create_appointment(request, db_alias):
        """
        Create a new appointment.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.

        Returns:
        - JsonResponse: JSON response with the created appointment details.
        """
        if request.method == 'POST':
            stylist_id = request.POST.get('stylist_id')
            service_id = request.POST.get('service_id')
            customer_name = request.POST.get('customer_name')
            discount = request.POST.get('discount', 0)
            appointment_date = request.POST.get('appointment_date')
            appointment = Appointment.objects.using(db_alias).create(
                stylist_id=stylist_id,
                service_id=service_id,
                customer_name=customer_name,
                discount=discount,
                appointment_date=appointment_date
            )
            return JsonResponse({
                "id": appointment.id,
                "stylist": appointment.stylist.name,
                "service": appointment.service.name,
                "customer_name": appointment.customer_name,
                "discount": appointment.discount,
                "appointment_date": appointment.appointment_date,
            })
        return HttpResponseNotAllowed(['POST'])
    
    @login_required
    def retrieve_appointment(request, db_alias, appointment_id):
        """
        Retrieve a specific appointment.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - appointment_id (int): The ID of the appointment to retrieve.

        Returns:
        - JsonResponse: JSON response with the retrieved appointment details.
        """
        appointment = get_object_or_404(Appointment.objects.using(db_alias), id=appointment_id)
        data = {
            "id": appointment.id,
            "stylist": appointment.stylist.name,
            "service": appointment.service.name,
            "customer_name": appointment.customer_name,
            "discount": appointment.discount,
            "appointment_date": appointment.appointment_date,
        }
        return JsonResponse(data)
    
    @login_required
    def update_appointment(request, db_alias, appointment_id):
        """
        Update a specific appointment.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - appointment_id (int): The ID of the appointment to update.

        Returns:
        - JsonResponse: JSON response with the updated appointment details.
        """
        if request.method == 'POST':
            appointment = get_object_or_404(Appointment.objects.using(db_alias), id=appointment_id)
            appointment.stylist_id = request.POST.get('stylist_id', appointment.stylist_id)
            appointment.service_id = request.POST.get('service_id', appointment.service_id)
            appointment.customer_name = request.POST.get('customer_name', appointment.customer_name)
            appointment.discount = request.POST.get('discount', appointment.discount)
            appointment.appointment_date = request.POST.get('appointment_date', appointment.appointment_date)
            appointment.save(using=db_alias)
            return JsonResponse({
                "id": appointment.id,
                "stylist": appointment.stylist.name,
                "service": appointment.service.name,
                "customer_name": appointment.customer_name,
                "discount": appointment.discount,
                "appointment_date": appointment.appointment_date,
            })
        return HttpResponseNotAllowed(['POST'])
    
    @login_required
    def delete_appointment(request, db_alias, appointment_id):
        """
        Delete a specific appointment.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - appointment_id (int): The ID of the appointment to delete.

        Returns:
        - JsonResponse: JSON response indicating the deletion status.
        """
        if request.method == 'POST':
            appointment = get_object_or_404(Appointment.objects.using(db_alias), id=appointment_id)
            appointment.delete(using=db_alias)
            return JsonResponse({"detail": "Appointment deleted."})
        return HttpResponseNotAllowed(['POST'])

class ServiceView:
    """
    A view that handles services.

    Methods:
    - list_services(request, db_alias): List all services.
    - create_service(request, db_alias): Create a new service.
    - retrieve_service(request, db_alias, service_id): Retrieve a specific service.
    - update_service(request, db_alias, service_id): Update a specific service.
    - delete_service(request, db_alias, service_id): Delete a specific service.
    """
    
    @login_required
    def list_services(request, db_alias):
        """
        List all services.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.

        Returns:
        - JsonResponse: JSON response with list of services.
        """
        services = Service.objects.using(db_alias).all()
        data = [{"id": service.id, "name": service.name, "price": str(service.price), "duration": service.duration} for service in services]
        return JsonResponse(data, safe=False)
    
    @login_required
    def create_service(request, db_alias):
        """
        Create a new service.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.

        Returns:
        - JsonResponse: JSON response with the created service details.
        """
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            duration = request.POST.get('duration')
            service = Service.objects.using(db_alias).create(name=name, price=price, duration=duration)
            return JsonResponse({"id": service.id, "name": service.name, "price": str(service.price), "duration": service.duration})
        return HttpResponseNotAllowed(['POST'])
    
    @login_required
    def retrieve_service(request, db_alias, service_id):
        """
        Retrieve a specific service.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - service_id (int): The ID of the service to retrieve.

        Returns:
        - JsonResponse: JSON response with the retrieved service details.
        """
        service = get_object_or_404(Service.objects.using(db_alias), id=service_id)
        data = {"id": service.id, "name": service.name, "price": str(service.price), "duration": service.duration}
        return JsonResponse(data)
    
    @login_required
    def update_service(request, db_alias, service_id):
        """
        Update a specific service.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - service_id (int): The ID of the service to update.

        Returns:
        - JsonResponse: JSON response with the updated service details.
        """
        if request.method == 'POST':
            service = get_object_or_404(Service.objects.using(db_alias), id=service_id)
            service.name = request.POST.get('name', service.name)
            service.price = request.POST.get('price', service.price)
            service.duration = request.POST.get('duration', service.duration)
            service.save(using=db_alias)
            return JsonResponse({"id": service.id, "name": service.name, "price": str(service.price), "duration": service.duration})
        return HttpResponseNotAllowed(['POST'])
    
    @login_required
    def delete_service(request, db_alias, service_id):
        """
        Delete a specific service.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - service_id (int): The ID of the service to delete.

        Returns:
        - JsonResponse: JSON response indicating the deletion status.
        """
        if request.method == 'POST':
            service = get_object_or_404(Service.objects.using(db_alias), id=service_id)
            service.delete(using=db_alias)
            return JsonResponse({"detail": "Service deleted."})
        return HttpResponseNotAllowed(['POST'])




class StylistView:
    """
    A view that handles stylists.

    Methods:
    - list_stylists(request, db_alias): List all stylists.
    - create_stylist(request, db_alias): Create a new stylist.
    - retrieve_stylist(request, db_alias, stylist_id): Retrieve a specific stylist.
    - update_stylist(request, db_alias, stylist_id): Update a specific stylist.
    - delete_stylist(request, db_alias, stylist_id): Delete a specific stylist.
    """
    
    @login_required
    def list_stylists(request, db_alias):
        """
        List all stylists.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.

        Returns:
        - JsonResponse: JSON response with list of stylists.
        """
        stylists = Stylist.objects.using(db_alias).all()
        data = [{"id": stylist.id, "name": stylist.name, "specialty": stylist.specialty} for stylist in stylists]
        return JsonResponse(data, safe=False)
    
    @login_required
    def create_stylist(request, db_alias):
        """
        Create a new stylist.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.

        Returns:
        - JsonResponse: JSON response with the created stylist details.
        """
        if request.method == 'POST':
            name = request.POST.get('name')
            specialty = request.POST.get('specialty')
            stylist = Stylist.objects.using(db_alias).create(name=name, specialty=specialty)
            return JsonResponse({"id": stylist.id, "name": stylist.name, "specialty": stylist.specialty})
        return HttpResponseNotAllowed(['POST'])
    
    @login_required
    def retrieve_stylist(request, db_alias, stylist_id):
        """
        Retrieve a specific stylist.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - stylist_id (int): The ID of the stylist to retrieve.

        Returns:
        - JsonResponse: JSON response with the retrieved stylist details.
        """
        stylist = get_object_or_404(Stylist.objects.using(db_alias), id=stylist_id)
        data = {"id": stylist.id, "name": stylist.name, "specialty": stylist.specialty}
        return JsonResponse(data)
    
    @login_required
    def update_stylist(request, db_alias, stylist_id):
        """
        Update a specific stylist.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - stylist_id (int): The ID of the stylist to update.

        Returns:
        - JsonResponse: JSON response with the updated stylist details.
        """
        if request.method == 'POST':
            stylist = get_object_or_404(Stylist.objects.using(db_alias), id=stylist_id)
            stylist.name = request.POST.get('name', stylist.name)
            stylist.specialty = request.POST.get('specialty', stylist.specialty)
            stylist.save(using=db_alias)
            return JsonResponse({"id": stylist.id, "name": stylist.name, "specialty": stylist.specialty})
        return HttpResponseNotAllowed(['POST'])
    
    @login_required
    def delete_stylist(request, db_alias, stylist_id):
        """
        Delete a specific stylist.

        Parameters:
        - request (HttpRequest): The HTTP request object.
        - db_alias (str): The database alias.
        - stylist_id (int): The ID of the stylist to delete.

        Returns:
        - JsonResponse: JSON response indicating the deletion status.
        """
        if request.method == 'POST':
            stylist = get_object_or_404(Stylist.objects.using(db_alias), id=stylist_id)
            stylist.delete(using=db_alias)
            return JsonResponse({"detail": "Stylist deleted."})
        return HttpResponseNotAllowed(['POST'])
