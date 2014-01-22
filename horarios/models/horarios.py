# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Horario(models.Model):
    hora = models.CharField(max_length=10)
    verbose_name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.verbose_name
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'
