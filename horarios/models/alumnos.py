# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    nombre = models.CharField(max_length=60, unique=True, db_index=True)
    matricula = models.EmailField(max_length=20, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'
