# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    nombre = models.CharField(max_length=60, unique=True, db_index=True)
    matricula = models.CharField(max_length=20, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s %s" % (self.nombre, self.matricula)
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'

class AlumnosClase(models.Model):
    alumno = models.ForeignKey('Alumno', related_name='clases')
    clase = models.ForeignKey('Clase', related_name='alumnos')
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s  %s" % (self.alumno.nombre,self.clase.id)
    
    #replace with your app name
    class Meta:
        app_label = 'horarios'
        unique_together = ['alumno', 'clase']
