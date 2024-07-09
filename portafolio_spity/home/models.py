from django.db import models

class Home(models.Model):
    # Campos del modelo para la página de inicio
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen_fondo = models.ImageField(upload_to='home/images/')
    # Otros campos según sea necesario

    def __str__(self):
        return self.titulo