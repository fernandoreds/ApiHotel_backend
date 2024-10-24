from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ganador/', UsuarioViewSet.as_view({'post': 'generar_ganador'}), name='generar_ganador'),
]
