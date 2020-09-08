from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name =  "Titulo", max_length = 200)
    content = RichTextField(verbose_name = "Contenido") 
    order = models.SmallIntegerField(verbose_name= "Orden", default= 0)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "fecha de edicición")


    class Meta:
        verbose_name ="página"
        verbose_name_plural = "páginas"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title 
