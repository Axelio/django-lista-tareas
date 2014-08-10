# -*- coding: UTF8 -*-
from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    '''
    Clase para el almacenamiento de tareas
    '''
    titulo = models.CharField(max_length=100, verbose_name=u'título')
    categoria = models.ForeignKey('Categoria', verbose_name=u'categoría')
    descripcion = models.TextField(verbose_name=u'descripción')

    class Meta:
        db_table = u'tarea'

    def __unicode__(self):
        return u'%s' % (self.titulo)

class TareaDetalle(models.Model):
    '''
    Clase en la que se relacionan directamente
    el usuario con su tarea
    '''
    usuario = models.ForeignKey(User)
    tarea = models.ForeignKey('Tarea')
    cumplida = models.BooleanField()
    fecha = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'tarea_detalle'
        verbose_name = 'tarea detalle'

    def __unicode__(self):
        return u'%s: %s' % (self.usuario, self.tarea)
    

class Categoria(models.Model):
    '''
    Clase para establecer el nombre de una categoria
    '''
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = u'categoria'
        verbose_name = 'categoría'

    def __unicode__(self):
        return u'%s' % (self.nombre)
