from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# --- USUARIO PERSONALIZADO ---
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('mecanico', 'Mecánico'),
        ('usuario', 'Usuario'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='usuario')

    def __str__(self):
        return self.username


# --- EQUIPO ---
class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    fecha_compra = models.DateField(null=True, blank=True)
    horas_uso_total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


# --- MANTENIMIENTO ---
class Mantenimiento(models.Model):
    TIPOS_PM = [
        ('PM1', 'Preventivo 1'),
        ('PM2', 'Preventivo 2'),
        ('PM3', 'Preventivo 3'),
    ]
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=4, choices=TIPOS_PM)
    fecha_programada = models.DateField()
    fecha_realizado = models.DateField(null=True, blank=True)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"{self.equipo.nombre} - {self.tipo}"


# --- INFORME MECÁNICO ---
class InformeMecanico(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField()

    def __str__(self):
        return f"Informe {self.equipo.nombre} - {self.fecha}"


# --- CHECKLIST ---
class Checklist(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    realizado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    estado = models.JSONField()  # Diccionario con el checklist

    def __str__(self):
        return f"Checklist {self.equipo.nombre} - {self.fecha}"


# --- USO DE EQUIPO ---
class UsoEquipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} usa {self.equipo.nombre}"


# --- RESERVAS ---
class Reserva(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    horas_reserva = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Reserva {self.equipo.nombre} por {self.usuario.username}"
