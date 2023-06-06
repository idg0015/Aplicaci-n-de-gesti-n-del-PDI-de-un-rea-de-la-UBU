import math

from flask import render_template, request, flash, redirect, url_for

from forms import FormGrupo, FormCursoAsignatura
from models.Curso import Curso
from models.CursoAsignatura import CursoAsignatura, Modalidad
from models.Grupo import Grupo, Tipo
from utils.db import db


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('grupo_bp.index_route'), 'Grupos'),
    ]
    # info = CursoAsignatura.get_all_json()
    form = FormCursoAsignatura()
    return render_template('grupos/index.html', cursos=Curso.get_all(), form=form, breadcrumbs=breadcrumbs)


def get_all_json():
    if request.method == "POST":
        return CursoAsignatura.get_all_json(request.form.get('id'))


def get_all_json_hours():
    if request.method == "POST":
        return Grupo.get_all_json_hours(request.form.get('id'))


def add():
    form = FormGrupo()
    if form.validate_on_submit():
        curso_asignatura = CursoAsignatura.get_with_id(form.id_curso_asignatura.data)
        if curso_asignatura is not None:
            create_check_grupos(curso_asignatura.id, form.tipo.data)
        else:
            flash('Asignatura no encontrada en el curso', 'alert alert-danger alert-dismissible fade show')
        return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=curso_asignatura.id))
    return render_template('cursos/modal.html', form=form)


def create_check_grupos(id_curso_asignatura, tipoNuevo):
    curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
    n_g_t = curso_asignatura.num_grupos_teoricos()
    n_g_p = curso_asignatura.num_grupos_practicos()

    if tipoNuevo == Tipo.Teorico.value:
        n_g_t += 1
        grupos_practicos_por_teorico = math.floor(n_g_p / n_g_t)
        grupos_practicos_restantes = n_g_p % n_g_t

        # Añado el nuevo grupo teórico
        nombre_nuevo = n_g_t
        if curso_asignatura.modalidad == Modalidad.Ingles.value:
            nombre_nuevo = n_g_t + 79
        elif curso_asignatura.modalidad == Modalidad.Online.value:
            nombre_nuevo = n_g_t + 89

        nuevo = Grupo(nombre=nombre_nuevo, tipo=tipoNuevo, id_curso_asignatura=curso_asignatura.id)
        flash('Grupo creado correctamente', 'alert alert-success alert-dismissible fade show')
        db.session.add(nuevo)

        change_names(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes, False)

    elif tipoNuevo == Tipo.Practico.value:
        if n_g_t > 0:
            n_g_p += 1
            grupos_practicos_por_teorico = math.floor(n_g_p / n_g_t)
            grupos_practicos_restantes = n_g_p % n_g_t
            change_names(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes, True)
        else:
            flash('No se puede crear un grupo práctico sin que exista al menos un grupo teórico',
                  'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=curso_asignatura.id))

    db.session.commit()


def change_names(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes, new_p=False):
    nombres_practicos = []
    for i in range(n_g_t):
        inicio_nombre = 100 * (i + 1) + 1
        nombre = i + 1
        if curso_asignatura.modalidad == Modalidad.Ingles.value:
            nombre = i + 80
            inicio_nombre = nombre * 10 + 1
        elif curso_asignatura.modalidad == Modalidad.Online.value:
            nombre = i + 90
            inicio_nombre = nombre * 10 + 1

        num_grupos_practicos_teorico = grupos_practicos_por_teorico
        if i < grupos_practicos_restantes:
            num_grupos_practicos_teorico += 1

        fin_nombre = inicio_nombre + num_grupos_practicos_teorico - 1

        for j in range(inicio_nombre, fin_nombre + 1):
            nombres_practicos.append(j)

    for grupo in curso_asignatura.grupos:
        if grupo.tipo == Tipo.Practico.value:
            grupo.nombre = nombres_practicos.pop(0)

    if new_p:
        nuevo = Grupo(nombre=nombres_practicos.pop(0), tipo=Tipo.Practico.value,
                      id_curso_asignatura=curso_asignatura.id)
        flash('Grupo creado correctamente', 'alert alert-success alert-dismissible fade show')
        db.session.add(nuevo)


def change_names_delete(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes):
    nombres_practicos = []
    nombres_teoricos = []
    for i in range(n_g_t):
        inicio_nombre = 100 * (i + 1) + 1
        nombre = i + 1
        if curso_asignatura.modalidad == Modalidad.Ingles.value:
            nombre = i + 80
            inicio_nombre = nombre * 10 + 1
        elif curso_asignatura.modalidad == Modalidad.Online.value:
            nombre = i + 90
            inicio_nombre = nombre * 10 + 1

        nombres_teoricos.append(nombre)
        num_grupos_practicos_teorico = grupos_practicos_por_teorico
        if i < grupos_practicos_restantes:
            num_grupos_practicos_teorico += 1

        fin_nombre = inicio_nombre + num_grupos_practicos_teorico - 1

        for j in range(inicio_nombre, fin_nombre + 1):
            nombres_practicos.append(j)

    for grupo in curso_asignatura.grupos:
        if grupo.tipo == Tipo.Practico.value:
            grupo.nombre = nombres_practicos.pop(0)
        else:
            grupo.nombre = nombres_teoricos.pop(0)


def delete(id_grupo):
    grupo = Grupo.get_with_id(id_grupo)
    id_curso_asignatura = grupo.id_curso_asignatura
    if grupo is not None:
        db.session.delete(grupo)
        db.session.flush()
        curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)

        n_g_t = curso_asignatura.num_grupos_teoricos()
        n_g_p = curso_asignatura.num_grupos_practicos()
        if len(grupo.plazas) == 0:
            if n_g_t > 0:
                grupos_practicos_por_teorico = math.floor(n_g_p / n_g_t)
                grupos_practicos_restantes = n_g_p % n_g_t
                change_names_delete(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes)
            else:
                if len(curso_asignatura.grupos) > 0:
                    flash('No se puede eliminar el último grupo teórico si tiene grupos prácticos. Elimínelos antes',
                          'alert alert-danger alert-dismissible fade show')
                    return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=id_curso_asignatura))
        else:
            flash('No se puede eliminar un grupo con plazas asignadas', 'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=id_curso_asignatura))
        db.session.commit()
        flash('Grupo eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    else:
        flash('Grupo no encontrado', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=id_curso_asignatura))
