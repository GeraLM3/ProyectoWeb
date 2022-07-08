from datetime import datetime
from decimal import Clamped
from django.contrib import admin
from .models import Servicios
# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')




admin.site.register(Servicios, ServiciosAdmin)

#ModelAdmin permite hacer cambios en los modelos que se trabajan en el panel de administracion