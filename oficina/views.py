from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import viewsets,  generics
from oficina.models import Cliente, Funcionario, Servico, ServicoRealizado, Veiculo
from oficina.serializer import ClienteSerializer, FuncionarioSerializer, ServicoSerializer, VeiculoSerializer,ListaVeiculosClientesSerializer,ServicoRealizadoSerializer, ServicosPorVeiculoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    "Clientes cadastrados"
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    "Funcionários cadastrados"
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    "Serviços cadastrados que podem ser realizados"
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    "Veículos cadastrados"
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class ListaVeiculosClientes(generics.ListAPIView):
    "Veículos de um respectivo cliente"
    def get_queryset(self):
        queryset = Veiculo.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVeiculosClientesSerializer

class ServicosPorVeiculo(generics.ListAPIView):
    "Serviços que um respectivo veículo recebeu"
    def get_queryset(self):
        queryset = ServicoRealizado.objects.filter(veiculo_id=self.kwargs['pk'])
        return queryset
    serializer_class = ServicosPorVeiculoSerializer


class ServicosRealizados(generics.ListAPIView):
    "Serviços que um respectivo funcionário realizou"
    def get_queryset(self):
        queryset = ServicoRealizado.objects.filter(funcionario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ServicoRealizadoSerializer
    