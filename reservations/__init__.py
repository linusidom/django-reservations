
# from reservations.forms import TemplatedForm
# from django.contrib import admin
# Default reservation model
# reservationModel = SimpleReservation




# def get_form():
#     """Returns templated model form for model that is currently set as reservationModel"""
#     pass


# def update_model(newModel, newAdmin=None):
#     """Update reservationModel variable and update Django admin to include it"""
#     global reservationModel
#     reservationModel = newModel
#     from django.contrib import admin
#     if not reservationModel in admin.site._registry:
#         admin.site.register(reservationModel, DefaultReservationAdmin if not newAdmin else newAdmin)
