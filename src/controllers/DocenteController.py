from flask import render_template
from models.Docente import Docente


def index():
    docentes = Docente.get_all_json()
    return render_template('docentes/index.html', docentes=docentes)
