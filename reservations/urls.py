from django.urls import path, re_path
# from django.views.generic.simple import *
from reservations.views import *
# Enable admin
from django.contrib import admin
# admin.autodiscover()

app_name = 'reservations'

urlpatterns =[
    re_path('month/(?P<month>\d*)/(?P<year>\d*)', MonthDetailView.as_view(), name='reservations_month'),
    path('reservation', Reservation.as_view(), name='reservations_reservation'),
    path('calendar', calendar_view, name='reservations_calendar'),
    path('holidays', get_holidays, name='reservations_holidays'),
]
