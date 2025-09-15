from rest_framework import viewsets, generics, permissions
from django.contrib.auth import get_user_model
from .models import *
from .serializers import *
from .user_serializers import UserRegisterSerializer
from .permissions import IsAdmin, IsMecanico, IsUsuario  # 👈 importa permisos personalizados
from rest_framework_simplejwt.views import TokenObtainPairView
from .token_serializers import CustomTokenObtainPairSerializer

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = []  # Cualquiera puede registrarse
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# ---------------- EQUIPOS ----------------
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]  # todos los logueados pueden ver


# ---------------- MANTENIMIENTOS ----------------
class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            return [IsMecanico() | IsAdmin()]
        return [permissions.IsAuthenticated()]


# ---------------- INFORMES MECÁNICOS ----------------
class InformeMecanicoViewSet(viewsets.ModelViewSet):
    queryset = InformeMecanico.objects.all()
    serializer_class = InformeMecanicoSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsMecanico() | IsAdmin()]
        return [permissions.IsAuthenticated()]


# ---------------- CHECKLISTS ----------------
class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsMecanico() | IsAdmin()]
        return [permissions.IsAuthenticated()]


# ---------------- USO DE EQUIPOS ----------------
class UsoEquipoViewSet(viewsets.ModelViewSet):
    queryset = UsoEquipo.objects.all()
    serializer_class = UsoEquipoSerializer

    def get_permissions(self):
        if self.action == "create":  # solo usuarios y admin pueden iniciar uso
            return [IsUsuario() | IsAdmin()]
        return [permissions.IsAuthenticated()]


# ---------------- RESERVAS ----------------
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def get_permissions(self):
        if self.action == "create":  # solo usuarios reservan
            return [IsUsuario() | IsAdmin()]
        return [permissions.IsAuthenticated()]


# ---------------- CAMBIO DE ROLES ----------------
class UserRoleUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRoleUpdateSerializer
    permission_classes = [permissions.IsAdminUser]  # solo admin puede cambiar roles
    lookup_field = "id"
