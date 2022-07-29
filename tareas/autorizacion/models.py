from re import T
from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser
# Create your models here.

class ManejoUsuario(BaseUserManager):
    #clase que sirve para manejar el comportamiento al crear el usuario con el comando
    def create_user(self , correo,nombre,apellido,password):
        if not correo:
            raise ValueError('El usuario debe tener obligatoriamente un correo')
        #normalizar el correo => elimina algun caracter especial y tmbn quita los espacios
        correo = self.normalize_email(correo)
        #creo mi nuevo usuario
        nuevoUsuario = self.model(correo=correo,nombre=nombre,apellido=apellido)
        #hashear la contraseña => genera un string aleatorio tomando como base la contraseña original
        nuevoUsuario.set_password(password)

        nuevoUsuario.save()
        return nuevoUsuario

    def create_superuser(self,correo,nombre,apellido,password):
        #creacion de un super usuario por consola, este metodo mandara a llamar cuando se haga la llamada del comando por consola
        nuevoUsuario = self.create_user(correo,nombre,apellido,password)
        #ahora modifico los valores que son correspondientes a un super usuario
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        nuevoUsuario.save()

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True, unique = True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.EmailField(unique=True)
    password = models.TextField()

    #Opcional y sirve si vamos a utilizar el panel administrativo(cms)
    # is_staff =>  indicara si el usuario es parte del staff que puede ingresar al CMS
    is_staff = models.BooleanField(default=False)

    # is_active => indicara si el usuario esta activo y por lo tanto puede tener acceso al CMS, si no esta activo aun asi sea staff no podra ingresar
    is_active = models.BooleanField(default=True)

    # python manage.py createsuperuser => comportamiento que va a tener
    
    objects = ManejoUsuario()

    #Servira para que en el login del panel administrativo nos pida el username que le coloquemos aca
    USERNAME_FIELD= 'correo'

    REQUIRED_FIELDS = ['nombre','apellido']

    class Meta:

        db_table='usuarios'

