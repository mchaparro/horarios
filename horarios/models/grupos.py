# -*- encoding: utf-8 -*-
from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=10, unique=True, db_index=True)
    verbose_name = models.CharField(max_length=40, unique=True, db_index=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.nombre,self.verbose_name)
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'
