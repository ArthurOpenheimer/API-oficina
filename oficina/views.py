from django.db.models.query import QuerySet
from rest_framework import viewsets,  generics
from oficina.models import Usuario, Servico, Veiculo
from oficina.serializer import UsuarioSerializer, ServicoSerializer, VeiculoSerializer,ListaVeiculosUsuariosSerializer

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

class ListaVeiculosUsuarios(generics.ListAPIView):
    """listando veiculos de um usuario"""
    def get_queryset(self):
        queryset = Veiculo.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVeiculosUsuariosSerializer