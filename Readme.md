
# DOCUMENTANDO NUESTRA APLICACION

- URL https://github.com/axnsan12/drf-yasg


# Desplegar muestra app en heroku

- Crear nuestro archivo Procfile en la raiz del proyecto
- Crear una base de datos en Heroku con JawsDB
- Crear nuestras variables de entorno en heroku con las credenciales de JAWSDB
- Inicializar git en nuestro proyecto con: git init
- Hacemos una conexion remota con heroku git remote -a <nombre-de-la-app>
- Desplegamos el proyecto con git add -A git commit -m "inicializacion" git push heroku master <nombre-de-la-rama>
- Hacemos una migracion de la bd con heroku run python manage.py migrate

# Configuracion de CORS
- Configuramos nuestra app para que pueda ser consumida desde cualquier lugar
- Instalamos el paquete cors pip install django-cors-headers
- Añadimos el paquete a nuestra aplicacion pip freeze >requirements.txt
- Añadimos las sigtes configuraciones en settings:
    INSTALLED_APPS = [
       ...,
      "corsheaders",
      ...,
    ]

    MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]