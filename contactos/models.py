from django.db import models

class contacto(models.Model):
    identificador = models.CharField(max_length = 50)
    nombre = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    referencias = models.CharField(max_length = 50)
    vinculo = models.CharField(max_length = 50)

    def __str__(self):
        return self.identificador + ' - ' + self.nombre
