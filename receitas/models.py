from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

# Create your models here.

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    foto_receita = models.ImageField(upload_to='foto/%d/%m/%y', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita