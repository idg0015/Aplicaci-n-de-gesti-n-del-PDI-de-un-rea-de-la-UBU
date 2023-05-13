import math
from copy import copy

from flask import render_template, jsonify, request, flash, redirect, url_for
from forms import FormCurso, UpdateYearCursoForm
from models.Asignatura import Asignatura
from models.Curso import Curso
from models.CursoAsignatura import CursoAsignatura, Modalidad
from models.Grupo import Grupo, Tipo
from utils.db import db


def index():
    cursos = Curso.get_all_json()
    form = UpdateYearCursoForm()
    return render_template('cursos/index.html', cursos=cursos, form=form)


def add():
    formulario = FormCurso()
    # asignaturas = Asignatura.get_asignaturas_groupby_titulacion()
    # asignaturas = Asignatura.get_all_json()
    if formulario.validate_on_submit():
        ano_inicio = formulario.ano_inicio.data
        curso = Curso(ano_inicio=ano_inicio)
        db.session.add(curso)
        db.session.flush()

        # Curso_Asignatura
        alumnos_presencial = formulario.n_a_p.data
        alumnos_ingles = formulario.n_a_i.data
        alumnos_online = formulario.n_a_o.data

        for id_asignatura in formulario.id_asignaturas.data[0].split(','):
            if alumnos_presencial > 0:
                num_grupos_teoricos = formulario.n_g_t_p.data
                num_grupos_practicos = formulario.n_g_p_p.data
                create_relation(num_grupos_teoricos, num_grupos_practicos, id_asignatura, curso.id, alumnos_presencial,
                                Modalidad.Presencial)

            if alumnos_ingles > 0:
                num_grupos_teoricos = formulario.n_g_t_i.data
                num_grupos_practicos = formulario.n_g_p_i.data
                create_relation(num_grupos_teoricos, num_grupos_practicos, id_asignatura, curso.id, alumnos_ingles,
                                Modalidad.Ingles)

            if alumnos_online > 0:
                num_grupos_teoricos = formulario.n_g_t_o.data
                num_grupos_practicos = formulario.n_g_p_o.data
                create_relation(num_grupos_teoricos, num_grupos_practicos, id_asignatura, curso.id, alumnos_online,
                                Modalidad.Online)

        db.session.commit()
        flash('Curso creado correctamente', 'alert alert-success alert-dismissible fade show')

        return redirect(url_for('curso_bp.index'))
    return render_template('cursos/form.html', form=formulario, asignaturas=[])


def create_relation(n_g_t, n_g_p, id_asignatura, id_curso, alumnos, modalidad):
    curso_asignatura = CursoAsignatura(modalidad=modalidad.value,
                                       num_alumnos_previstos=alumnos,
                                       num_grupos_teoricos_previstos=n_g_t,
                                       num_grupos_practicos_previstos=n_g_p,
                                       id_curso=id_curso, id_asignatura=id_asignatura)
    db.session.add(curso_asignatura)
    db.session.flush()

    grupos_practicos_por_teorico = math.floor(n_g_p / n_g_t)
    grupos_practicos_restantes = n_g_p % n_g_t

    for i in range(n_g_t):
        inicio_nombre = 100 * (i + 1) + 1
        nombre = i + 1

        if modalidad == Modalidad.Ingles:
            nombre = i + 80
            inicio_nombre = nombre * 10 + 1
        elif modalidad == Modalidad.Online:
            nombre = i + 90
            inicio_nombre = nombre * 10 + 1

        grupo = Grupo(nombre=nombre, tipo=Tipo.Teorico.value, id_curso_asignatura=curso_asignatura.id)
        db.session.add(grupo)

        num_grupos_practicos_teorico = grupos_practicos_por_teorico
        if i < grupos_practicos_restantes:
            num_grupos_practicos_teorico += 1

        fin_nombre = inicio_nombre + num_grupos_practicos_teorico - 1

        for j in range(inicio_nombre, fin_nombre + 1):
            grupo_practico = Grupo(nombre=j, tipo=Tipo.Practico.value, id_curso_asignatura=curso_asignatura.id)
            db.session.add(grupo_practico)


def render_sortable():
    if request.method == "POST":
        asignaturas = Asignatura.get_asignaturas_by_titulacion(request.form.get('id_titulacion'))
        return jsonify(render_template('cursos/sortable.html', asignaturas=asignaturas))


def delete(id_curso):
    curso = Curso.get_curso(id_curso)
    if curso is not None:
        db.session.delete(curso)
        db.session.commit()
        flash('Curso eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    else:
        flash('Curso no encontrado', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('curso_bp.index'))


def update_year():
    form = UpdateYearCursoForm()
    if form.validate_on_submit():
        curso = Curso.get_curso(form.id_curso.data)
        if curso is not None:
            curso.ano_inicio = form.year.data
            db.session.commit()
            flash('Curso actualizado correctamente', 'alert alert-success alert-dismissible fade show')
        else:
            flash('Curso no encontrado', 'alert alert-danger alert-dismissible fade show')
        return redirect(url_for('curso_bp.index'))
    return render_template('cursos/modal.html', form=form)



def duplicate(id_curso):
    try:
        curso = Curso.get_curso(id_curso)
        if curso is not None:
            with db.session.begin_nested():
                # Creo el nuevo curso copiando el anteior y le sumo 1 al año de inicio
                nuevo_curso = Curso(ano_inicio=int(curso.ano_inicio) + 1)
                db.session.add(nuevo_curso)
                db.session.flush()

                # Recojo los curso_asignatura del curso a duplicar
                curso_asignaturas = curso.asignaturas

                for curso_asignatura in curso_asignaturas:
                    # Recojo los grupos del curso_asignatura
                    grupos = curso_asignatura.grupos
                    nuevo_curso_asignatura = CursoAsignatura(id_asignatura=curso_asignatura.id_asignatura,
                                                             id_curso=nuevo_curso.id,
                                                             modalidad=curso_asignatura.modalidad,
                                                             num_alumnos_previstos=curso_asignatura.num_alumnos_previstos,
                                                             num_grupos_teoricos_previstos=curso_asignatura.num_grupos_teoricos_previstos,
                                                             num_grupos_practicos_previstos=curso_asignatura.num_grupos_practicos_previstos)
                    db.session.add(nuevo_curso_asignatura)
                    db.session.flush()

                    for grupo in grupos:
                        nuevo_grupo = Grupo(nombre=grupo.nombre, tipo=grupo.tipo,
                                            id_curso_asignatura=nuevo_curso_asignatura.id)
                        db.session.add(nuevo_grupo)
                db.session.commit()
                flash('Curso duplicado correctamente', 'alert alert-success alert-dismissible fade show')
        else:
            flash('Curso no encontrado', 'alert alert-danger alert-dismissible fade show')
    except Exception as e:
        db.session.rollback()
        flash('Error al duplicar el curso: ' + str(e), 'alert alert-danger alert-dismissible fade show')

    return redirect(url_for('curso_bp.index'))
