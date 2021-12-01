from django.db import models
from django.db.models import fields
from rest_framework import serializers
from oficina.admin import Usuario
from oficina.models import Usuario, Servico, Veiculo


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'cpf', 'endereco']

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    nome_usuario = serializers.ReadOnlyField(source='usuario.nome')
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'tipo', 'ano', 'nome_usuario']

class ListaVeiculosUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'tipo', 'ano']