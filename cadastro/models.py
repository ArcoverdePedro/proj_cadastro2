from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome