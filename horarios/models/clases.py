# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Clase(models.Model):
    hora = models.ForeignKey('Horario', related_name='clases')
    grupo = models.ForeignKey('Grupo', related_name='clases')
    salon = models.ForeignKey('Salon', related_name='clases')
    fecha = models.DateField()
    
    def __unicode__(self):
        return "%s %s %s %s - %s" % (self.grupo.nombre,self.salon.nombre,self.fecha,self.hora.verbose_name, self.id)
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'
        unique_together = ['hora','salon','fecha']