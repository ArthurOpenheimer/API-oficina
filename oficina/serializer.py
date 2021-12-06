from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.viewsets import ReadOnlyModelViewSet
from oficina.admin import Cliente, Funcionario
from oficina.models import Cliente, Funcionario, Servico, Veiculo


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'endereco']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'cpf', 'endereco']

class ServicoSerializer(serializers.ModelSerializer):
    data = serializers.DateField(format='%d/%m/%Y')
    class Meta:
        model = Servico
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'modelo', 'marca', 'tipo', 'ano', 'cliente']

class ListaVeiculosClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'tipo', 'ano']

class ServicoRealizadoSerializer(serializers.ModelSerializer):
    data = serializers.DateField(format='%d/%m/%Y')
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'valor', 'veiculo', 'data']   

class ServicosRealizadosPorVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['nome', 'valor']

class ValorTotalServicosRealizadosPorVeiculoSerializer(serializers.Serializer):
    valor_total = serializers.ReadOnlyField(source = 'veiculo.valor')
    class Meta:
        fields = ['valor_total']
