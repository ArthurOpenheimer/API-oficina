from django.contrib import admin
from django.urls import path, include
from oficina.views import ClienteViewSet, FuncionarioViewSet, ServicoViewSet, VeiculoViewSet, ListaVeiculosClientes
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet, basename = 'cliente')
router.register('funcionario', FuncionarioViewSet, basename = 'funcionario')
router.register('servico', ServicoViewSet, basename = 'servico')
router.register('veiculo', VeiculoViewSet, basename = 'veiculo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/veiculos/', ListaVeiculosClientes.as_view()),
]
