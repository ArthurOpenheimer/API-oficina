from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)

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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo

    