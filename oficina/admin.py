from re import search
from django.contrib import admin
from .models import Usuario, Servico, Veiculo

admin.site.register(Usuario)
admin.site.register(Servico)
admin.site.register(Veiculo)

class Usuario(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'endereco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


class Servico(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

class Veiculo(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'marca', 'tipo', 'ano')
    list_display_links = ('id','modelo')
    search_fields = ('modelo',)

