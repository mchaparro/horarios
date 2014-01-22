# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Horarios(models.Model):
    nombre = models.CharField(max_length=30, unique=True, db_index=True)
    fecha = models.DateField(auto_now_add=False, null=False, default="")
    def __unicode__(self):
        return self.nombre
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'
