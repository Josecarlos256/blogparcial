from django.db import models

class Publicaciones(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha = models.DateField()
    autor = models.TextField()

    def __str__(self):
        return self.name
