from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from equipos.models import Equipo, Mantenimiento, InformeMecanico, Checklist, UsoEquipo, Reserva

class Command(BaseCommand):
    help = "Inicializa roles y permisos"

    def handle(self, *args, **kwargs):
        # Crear grupos
        admin_group, _ = Group.objects.get_or_create(name="Administrador")
        mecanico_group, _ = Group.objects.get_or_create(name="Mecanico")
        usuario_group, _ = Group.objects.get_or_create(name="Usuario")

        # Obtener permisos de los modelos
        modelos = [Equipo, Mantenimiento, InformeMecanico, Checklist, UsoEquipo, Reserva]

        for modelo in modelos:
            permisos = Permission.objects.filter(content_type__app_label="equipos", content_type__model=modelo._meta.model_name)

            if modelo == Equipo:
                admin_group.permissions.add(*permisos)  # Solo admin maneja equipos
            elif modelo in [Mantenimiento, InformeMecanico, Checklist]:
                admin_group.permissions.add(*permisos)
                mecanico_group.permissions.add(*permisos)
            elif modelo in [UsoEquipo, Reserva]:
                admin_group.permissions.add(*permisos)
                usuario_group.permissions.add(*permisos)

        self.stdout.write(self.style.SUCCESS("✅ Roles y permisos creados correctamente"))
