from django.contrib import admin
from cars.models import Car

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CAR INFO', {'fields':['brand']}),
        ('YEAR INFO', {'fields':['year']})
    ]

admin.site.register(Car,CarAdmin)
