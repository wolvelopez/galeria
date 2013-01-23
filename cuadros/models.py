from django.db import models

class cuadros(models.Model):
	nombre = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to="images")
	descripcion = models.CharField(max_length=300)
	precio = models.FloatField()


