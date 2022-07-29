
from django.db import models
from autorizacion.models import Usuario
class Tarea(models.Model):
    estadoOpciones =[('POR_HACER','POR_HACER'),('HACIENDO','HACIENDO'),('HECHO','HECHO')]
    id = models.AutoField (primary_key=True, unique = True)
    nombre = models.CharField(max_length = 100 ,null = False)
    descripcion = models.TextField(null=True)
    fechaVencimiento = models.DateTimeField(db_column='fecha_vencimiento',null= False)
    estado = models.CharField(choices =estadoOpciones,max_length=10,default='POR_HACER')

    # crear la relacion entre el modelo tarea y usuario
    # on_delete=> sirve para indicar que accion se debe realizar sobre los registros que pertenecen a ese registro a eliminar y sus valores pueden ser:
    #CASCADE => se elimina el usuario y se procede a eliminar sus tareas
    # PROTECT => evita la eliminacion del usuario y emitira un error
    # SET_NULL => elimina al usuario y a todas sus tareas les cambia el valor de usuario_id a NULL
    # SET_DEFAULT => elimina el usuario y modifica su valor a un valor por defecto

    # Related_name => sirve para que a raiz del modelo usuario este cree un atributo en la clase Usuario para poder acceder a todas sus tareas si no se define, el valor predeterminado sera usuario_set_tarea
    UsuarioId = models.ForeignKey(to = Usuario,related_name='tareas',db_column='usuario_id',on_delete=models.CASCADE)

    class Meta:
        db_table = 'tareas'
        # El ordenamiento se dara de manera descendiente por la fecha de vencimiento y de manera ascendente en el campo de nombre
        ordering = ['-fechaVencimiento','nombre']