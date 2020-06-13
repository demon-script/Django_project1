from django.db import models
from unittest.util import _MAX_LENGTH
from pip._vendor.chardet.cli.chardetect import description_of

# Create your models here.
class New_Project(models.Model):
    title = models.CharField(max_length = 80, verbose_name = 'Nombre del Proyecto')
    description = models.TextField(verbose_name = 'Descripción')
    more_info = models.URLField(null = True, blank = True,verbose_name='Sitio Web')
    image = models.ImageField(upload_to = 'projects',verbose_name = 'Imagen')
    
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'F. Creación')
    modified = models.DateTimeField(auto_now = True, verbose_name = 'F. Modificación')
    
    class Meta():
        verbose_name = "Mi Proyecto"
        verbose_name_plural = "Mis Proyectos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.title
    