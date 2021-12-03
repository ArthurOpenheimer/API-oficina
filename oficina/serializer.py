from django.db import models
from django.db.models import fields
from rest_framework import serializers
from oficina.admin import Cliente, Funcionario
from oficina.models import Cliente, Funcionario, Servico, Veiculo, ServicoRealizado


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'endereco']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'cpf', 'endereco']

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'valor']

class VeiculoSerializer(serializers.ModelSerializer):
    nome_cliente = serializers.ReadOnlyField(source='cliente.nome')
    class Meta:
        model = Veiculo
        fields = ['id', 'modelo', 'marca', 'tipo', 'ano', 'nome_cliente']

class ListaVeiculosClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'tipo', 'ano']

class ServicoRealizadoSerializer(serializers.ModelSerializer):
    nome_servico = serializers.ReadOnlyField(source='servico.nome')
    valor_servico = serializers.ReadOnlyField(source='servico.valor')
    class Meta:
        model = ServicoRealizado
        fields = ['id', 'nome_servico', 'valor_servico', 'veiculo', 'data']   

class ServicosRealizadosPorVeiculoSerializer(serializers.ModelSerializer):
    nome_servico = serializers.ReadOnlyField(source='servico.nome')
    valor_servico = serializers.ReadOnlyField(source='servico.valor')
    class Meta:
        model = ServicoRealizado   
        fields = ['nome_servico', 'valor_servico']
