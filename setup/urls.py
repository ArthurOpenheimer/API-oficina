from django.contrib import admin
from django.urls import path, include
from oficina import views
from oficina.views import ClienteViewSet, FuncionarioViewSet, ServicoViewSet, VeiculoViewSet, ListaVeiculosClientes, ServicosRealizados, ServicosRealizadosPorVeiculo, ValorTotal
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet, basename = 'clientes')
router.register('funcionario', FuncionarioViewSet, basename = 'funcionarios')
router.register('veiculo', VeiculoViewSet, basename = 'veiculos')
router.register('servico', ServicoViewSet, basename = 'servicos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/veiculos/', ListaVeiculosClientes.as_view()),
    path('funcionario/<int:pk>/servicos/', ServicosRealizados.as_view()),
    path('veiculo/<int:pk>/servicos/', ServicosRealizadosPorVeiculo.as_view()),
    path('veiculo/<int:pk>/servicos/valor/', ValorTotal.as_view(), name='valor_total'),
]
