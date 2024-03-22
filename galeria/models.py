from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descrição = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        """
        Retorna uma representação de string do objeto com o formato "Fotografia [nome={self.nome}]"
        """
        return f"Fotografia [nome={self.nome}]"
