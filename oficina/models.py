from django.db import models
from datetime import datetime

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    ano = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo

class ServicoRealizado(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)    
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)  
    data = models.DateField(default=datetime.today())
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

   