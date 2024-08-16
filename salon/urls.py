from django.urls import path
from .views import StylistView, ServiceView, AppointmentView

urlpatterns = [
    # Stylist CRUD
    path('stylists/<str:db_alias>/', StylistView.list_stylists, name='list_stylists'),
    path('stylists/<str:db_alias>/create/', StylistView.create_stylist, name='create_stylist'),
    path('stylists/<str:db_alias>/<int:stylist_id>/', StylistView.retrieve_stylist, name='retrieve_stylist'),
    path('stylists/<str:db_alias>/<int:stylist_id>/update/', StylistView.update_stylist, name='update_stylist'),
    path('stylists/<str:db_alias>/<int:stylist_id>/delete/', StylistView.delete_stylist, name='delete_stylist'),

    # Service CRUD
    path('services/<str:db_alias>/', ServiceView.list_services, name='list_services'),
    path('services/<str:db_alias>/create/', ServiceView.create_service, name='create_service'),
    path('services/<str:db_alias>/<int:service_id>/', ServiceView.retrieve_service, name='retrieve_service'),
    path('services/<str:db_alias>/<int:service_id>/update/', ServiceView.update_service, name='update_service'),
    path('services/<str:db_alias>/<int:service_id>/delete/', ServiceView.delete_service, name='delete_service'),

    # Appointment CRUD
    path('appointments/<str:db_alias>/', AppointmentView.list_appointments, name='list_appointments'),
    path('appointments/<str:db_alias>/create/', AppointmentView.create_appointment, name='create_appointment'),
    path('appointments/<str:db_alias>/<int:appointment_id>/', AppointmentView.retrieve_appointment, name='retrieve_appointment'),
    path('appointments/<str:db_alias>/<int:appointment_id>/update/', AppointmentView.update_appointment, name='update_appointment'),
    path('appointments/<str:db_alias>/<int:appointment_id>/delete/', AppointmentView.delete_appointment, name='delete_appointment'),
]