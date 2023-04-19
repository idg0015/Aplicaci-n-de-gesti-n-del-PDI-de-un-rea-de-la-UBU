from flask import render_template
from models.Curso import Curso
from models.CursoAsignatura import CursoAsignatura


def index():
    cursos = Curso.get_all_json()
    return render_template('cursos/index.html', cursos=cursos)
