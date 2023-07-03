from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
