from django.db import models
from consumidores.models import Consumidor

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Pendencia(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.consumidor.nome} - {self.produto.nome}"
    
class Emprestimo(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_emprestimo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.consumidor.nome} - {self.produto.nome}"
    
    def save(self, *args, **kwargs):
        self.produto.quantidade -= self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.produto.quantidade += self.quantidade
        self.produto.save()
        super().delete(*args, **kwargs)