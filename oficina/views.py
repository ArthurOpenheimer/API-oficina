from django.db.models.query import QuerySet
from rest_framework import serializers, viewsets
from oficina.models import Usuario, Servico, Veiculo
from oficina.serializer import UsuarioSerializer, ServicoSerializer, VeiculoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """chique"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    """mec"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    """vrum vrum"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer