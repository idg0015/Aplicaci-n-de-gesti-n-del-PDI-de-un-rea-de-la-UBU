from flask import render_template
from forms import FormCurso
from models.Asignatura import Asignatura
from models.Curso import Curso
from models.CursoAsignatura import CursoAsignatura
from utils.db import db


def index():
    cursos = Curso.get_all_json()
    return render_template('cursos/index.html', cursos=cursos)


def add():
    formulario = FormCurso()
    asignaturas = Asignatura.get_all_json()
    if formulario.validate_on_submit():
        ano_inicio = formulario.ano_inicio.data
        curso = Curso(ano_inicio=ano_inicio)
        db.session.add(curso)
        for id_asignatura in formulario.id_asignaturas.data:
            curso_asignatura = CursoAsignatura(id_curso=curso.id, id_asignatura=id_asignatura)
            db.session.add(curso_asignatura)

        return render_template('cursos/index.html')

    return render_template('cursos/form.html', form=formulario, asignaturas=asignaturas)


def add2():
    formulario = FormCurso()
    if formulario.validate_on_submit():
        ano_inicio = formulario.ano_inicio.data
        curso = Curso(ano_inicio=ano_inicio)
        curso.save()
        return render_template('cursos/index.html')

    return render_template('cursos/form.html', form=formulario)
