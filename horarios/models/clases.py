# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Clase(models.Model):
    hora = models.ForeignKey('Horario', related_name='clases')
    grupo = models.ForeignKey('Grupo', related_name='clases')
    salon = models.ForeignKey('Salon', related_name='clases')
    fecha = models.DateField()
    estatus = models.CharField(max_length = 20, choices = (('activa','activa'),('cancelada','cancelada')), default='activa')
    
    def __unicode__(self):
        return "%s %s %s %s %s %s" % (self.id,self.grupo.nombre,self.salon.nombre,self.fecha,self.hora.verbose_name, self.estatus)
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'

    def save(self, *args, **kwargs):
        salon_en_uso = Clase.objects.filter(hora=self.hora,grupo=self.grupo,salon=self.salon,fecha=self.fecha,estatus='activa')
        if salon_en_uso and self.estatus=='activa':
            raise Exception('Ya existe una clase activa a esa hora y en ese salon, si deseas cambiar la clase de hora es necesario cancelar la clase actual')
        super(Clase, self).save(*args, **kwargs)