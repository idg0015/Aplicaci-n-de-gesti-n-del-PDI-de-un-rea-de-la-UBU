from flask import render_template
from models.Departamento import Departamento


def index():
    departamentos = Departamento.get_all_json()
    return render_template('departamentos/index.html', departamentos=departamentos)
