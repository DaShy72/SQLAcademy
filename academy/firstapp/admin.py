from django.contrib import admin
from .models import Company, Passenger, Pass_in_trip, Trip

admin.site.register(Company)
admin.site.register(Passenger)
admin.site.register(Pass_in_trip)
admin.site.register(Trip)

