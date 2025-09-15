from django.contrib.auth.models import  Group
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=["Administrador", "Mecanico", "Usuario"])

    class Meta:
        model = User
        fields = ["username", "email", "password", "role"]

    def create(self, validated_data):
        role = validated_data.pop("role")
        password = validated_data.pop("password")

        # Crear usuario
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        # Asignar rol (grupo)
        group, _ = Group.objects.get_or_create(name=role)
        user.groups.add(group)

        return user
