from django.db import models

# Create your models here.
class Service(models.Model):
    tittle = models.CharField(max_length = 200, verbose_name ="Titulo")  
    subtittle = models.CharField(max_length = 200, verbose_name ="Subtitulo") 
    content = models.TextField(verbose_name= "Contenido")
    image = models.ImageField(verbose_name ="Imagen",upload_to = "services")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "fecha de edicición")

    class Meta:
        verbose_name ="servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.tittle    
