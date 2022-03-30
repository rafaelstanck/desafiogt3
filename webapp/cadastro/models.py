from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    observacao = models.TextField()

    def __str__(self):
        return self.nome
