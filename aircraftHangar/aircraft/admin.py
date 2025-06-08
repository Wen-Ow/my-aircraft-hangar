from django.contrib import admin
from .models import AircraftType, Category, Aircraft
# Register your models here.
admin.site.register(AircraftType)
admin.site.register(Category)
admin.site.register(Aircraft)
