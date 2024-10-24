# api/serializers.py
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'verificado', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Aquí puedes agregar lógica para encriptar la contraseña
        usuario = Usuario(**validated_data)
        usuario.save()
        return usuario
