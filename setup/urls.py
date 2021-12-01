from django.contrib import admin
from django.urls import path, include
from oficina.views import UsuarioViewSet, ServicoViewSet, VeiculoViewSet, ListaVeiculosUsuarios
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet, basename = 'usuario')
router.register('servico', ServicoViewSet, basename = 'servico')
router.register('veiculo', VeiculoViewSet, basename = 'veiculo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuario/<int:pk>/veiculos/', ListaVeiculosUsuarios.as_view()),
]
