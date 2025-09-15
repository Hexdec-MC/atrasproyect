from django.contrib import admin
from .models import Equipo, Mantenimiento, InformeMecanico, Checklist, UsoEquipo, Reserva

admin.site.register(Equipo)
admin.site.register(Mantenimiento)
admin.site.register(InformeMecanico)
admin.site.register(Checklist)
admin.site.register(UsoEquipo)
admin.site.register(Reserva)