from django.contrib import admin
from django.urls import path, include
from oficina.views import UsuarioViewSet, ServicoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet, basename = 'usuario')
router.register('servico', ServicoViewSet, basename = 'servico')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
