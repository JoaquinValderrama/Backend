from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Bienvenido a mi aplicacion con Flask :D'

alumnos = [
    {
        'nombre': 'Eduardo',
        'apellido' : 'De Rivero'
    },
    {
        'nombre' : 'Jorge',
        'apellido' : 'Garnica'
    }
]
@app.route('/alumnos')
def lista_alumnos():
    return {
        'alumnos' :alumnos
    }