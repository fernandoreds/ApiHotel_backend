from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
import random

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request):
        email = request.data.get('email')
        if Usuario.objects.filter(email=email).exists():
            return Response({"error": "El email ya está registrado."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generar_ganador(self, request):
        usuarios = list(Usuario.objects.filter(verificado=True))
        if not usuarios:
            return Response({"error": "No hay participantes verificados."}, status=status.HTTP_400_BAD_REQUEST)
        
        ganador = random.choice(usuarios)
        return Response({"ganador": ganador.nombre, "email": ganador.email}, status=status.HTTP_200_OK)
