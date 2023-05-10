from flask import render_template, jsonify, request
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
    # asignaturas = Asignatura.get_asignaturas_groupby_titulacion()
    # asignaturas = Asignatura.get_all_json()
    if formulario.validate_on_submit():
        ano_inicio = formulario.ano_inicio.data
        curso = Curso(ano_inicio=ano_inicio)
        db.session.add(curso)
        for id_asignatura in formulario.id_asignaturas.data:
            # alumnos_presencial = formulario.n_a_p.data
            # if alumnos_presencial > 0:
            #     grupos_teoria = formulario.n_g_t_p.data
            #     grupos_practica = formulario.n_g_p_p.data
            #     if grupos_teoria > 0:
            #         for i in range(grupos_teoria):

            curso_asignatura = CursoAsignatura(id_curso=curso.id, id_asignatura=id_asignatura)
            db.session.add(curso_asignatura)

        return render_template('cursos/index.html')

    return render_template('cursos/form.html', form=formulario, asignaturas=[])


def add2():
    formulario = FormCurso()
    if formulario.validate_on_submit():
        ano_inicio = formulario.ano_inicio.data
        curso = Curso(ano_inicio=ano_inicio)
        curso.save()
        return render_template('cursos/index.html')

    return render_template('cursos/form.html', form=formulario)


def render_sortable():
    if request.method == "POST":
        asignaturas = Asignatura.get_asignaturas_by_titulacion(request.form.get('id_titulacion'))
        return jsonify(render_template('cursos/sortable.html', asignaturas=asignaturas))
