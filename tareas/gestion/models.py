from unittest.util import _MAX_LENGTH
from django.db import models

class Tarea(models.Model):
    estadoOpciones =[('POR_HACER','POR_HACER'),('HACIENDO','HACIENDO'),('HECHO','HECHO')]
    id = models.AutoField (primary_key=True, unique = True)
    nombre = models.CharField(max_length = 100 ,null = False)
    descripcion = models.TextField(null=True)
    fechaVencimiento = models.DateTimeField(db_column='fecha_vencimiento',null= False)
    estado = models.CharField(choices =estadoOpciones,max_length=10,default='POR_HACER')

    class Meta:
        db_table = 'tareas'
        # El ordenamiento se dara de manera descendiente por la fecha de vencimiento y de manera ascendente en el campo de nombre
        ordering = ['-fechaVencimiento','nombre']