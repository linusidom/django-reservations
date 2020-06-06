from django.contrib import admin
from reservations.models import *

class DefaultReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    # list_filter = ('date',)
    date_hierarchy = 'date'

admin.site.register(Reservation, DefaultReservationAdmin)
admin.site.register(ReservationDay)
admin.site.register(Holiday)
