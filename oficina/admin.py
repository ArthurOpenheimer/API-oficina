from re import search
from django.contrib import admin
from .models import Cliente, Funcionario, Servico, Veiculo

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(Veiculo)

class Cliente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'endereco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

class Funcionario(admin.ModelAdmin):
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
