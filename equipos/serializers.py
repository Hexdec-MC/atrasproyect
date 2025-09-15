from rest_framework import serializers
from .models import Equipo, Mantenimiento, InformeMecanico, Checklist, UsoEquipo, Reserva
from .models import CustomUser
from django.contrib.auth import get_user_model


User = get_user_model()
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class InformeMecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformeMecanico
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'

class UsoEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsoEquipo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'usuario')
        )
        return user
    
class UserRoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'role']  # solo exponemos lo necesario
        read_only_fields = ['id', 'username']