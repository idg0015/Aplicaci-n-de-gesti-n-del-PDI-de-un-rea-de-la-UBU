from flask import render_template
from models.Asignatura import Asignatura
from models.Abreviatura import Abreviatura


def index():
    asignaturas = Asignatura.get_all_json()
    print(asignaturas)
    return render_template('asignaturas/index.html', asignaturas=asignaturas)
