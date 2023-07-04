from django.db import models

class Consumidor(models.Model):
    id_consumidor = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.email}"
    
    class Meta:
        db_table = 'consumidores_consumidor'
