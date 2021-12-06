from django.db.models import query, Sum
from django.db.models.query import QuerySet
from rest_framework import serializers, views, viewsets,  generics
from oficina.models import Cliente, Funcionario, Servico, Veiculo
from oficina.serializer import ClienteSerializer, FuncionarioSerializer, ServicoSerializer, VeiculoSerializer,ListaVeiculosClientesSerializer,ServicoRealizadoSerializer, ServicosRealizadosPorVeiculoSerializer, ValorTotalServicosRealizadosPorVeiculoSerializer
from django.views import generic
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.urls import reverse

class ClienteViewSet(viewsets.ModelViewSet):
    "Clientes cadastrados"
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    "Funcionários cadastrados"
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    "Serviços realizdos"
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

class ServicosRealizadosPorVeiculo(generics.ListAPIView):
    "Serviços realizados em um respectivo veículo"
    def get_queryset(self):
        queryset = Servico.objects.filter(veiculo_id=self.kwargs['pk'])
        return queryset
    serializer_class = ServicosRealizadosPorVeiculoSerializer

class ServicosRealizados(generics.ListAPIView):
    "Serviços que um respectivo funcionário realizou"
    def get_queryset(self):
        queryset = Servico.objects.filter(funcionario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ServicoRealizadoSerializer

class ValorTotal(views.APIView):
    "Valor total dos serviços realizados"
    def get(self,request, *args, **kwargs):  
        HttpResponseRedirect(reverse('valor_total', kwargs={'pk': self.kwargs['pk']}))
        servico_object = Servico.objects.filter(veiculo_id=self.kwargs['pk']).aggregate(valor_total = Sum('valor'))
        return Response(servico_object)