from flask import render_template, redirect, url_for, flash, request, jsonify, session

from forms import FormPlazaGrupo, FormPlazaGrupoUpdate
from models.Curso import Curso
from models.Docente import Docente
from models.Grupo import Grupo
from models.Plaza import Plaza
from models.PlazaGrupo import PlazaGrupo
from utils.db import db


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('horas_bp.index_route'), 'Horas'),
    ]
    has_modification_permission = Docente.get_docente(session['user_id']).modification_flag
    return render_template('horas/index.html', cursos=Curso.get_all(), breadcrumbs=breadcrumbs,
                           has_modification_permission=has_modification_permission)


# Función para mostrar las plazas de un grupo
def group_view(group_id):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('horas_bp.index_route'), 'Horas'),
        ('', 'Grupo'),
    ]
    group = Grupo.get_with_id(group_id)
    vacancies = PlazaGrupo.get_vacancies_group_json(group_id)
    form = FormPlazaGrupo()
    form_update = FormPlazaGrupoUpdate()
    has_modification_permission = Docente.get_docente(session['user_id']).modification_flag
    return render_template('horas/view.html', plazas=vacancies, grupo=group, form=form, form_update=form_update,
                           breadcrumbs=breadcrumbs, has_modification_permission=has_modification_permission)


# Función para vincular una plaza a un grupo con x horas
def assign_hours():
    form = FormPlazaGrupo()
    if form.validate_on_submit():
        vacant_id = form.vacant.data
        group_id = form.group_id.data
        hours = form.hours.data

        vacant = Plaza.get_plaza(vacant_id)
        group = Grupo.get_with_id(group_id)
        if vacant is None or group is None:
            flash('No se pudo asignar las horas', 'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('horas_bp.group_view_route', group_id=group_id))

        if PlazaGrupo.get_with_vacant_and_group_id(vacant_id, group_id) is not None:
            flash('Ya existe una asignación para la plaza seleccionada',
                  'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('horas_bp.group_view_route', group_id=group_id))

        vacant_group = PlazaGrupo(horas=hours, id_grupo=group_id, id_plaza=vacant_id)
        db.session.add(vacant_group)
        db.session.commit()
        flash('Horas asignadas correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('horas_bp.group_view_route', group_id=group_id))


# Función para eliminar una asociación de una plaza a un grupo
def delete(vacant_group_id):
    vacant_group = PlazaGrupo.get_with_id(vacant_group_id)
    if vacant_group is None:
        flash('No se pudo eliminar la asociación', 'alert alert-danger alert-dismissible fade show')
        return redirect(url_for('horas_bp.index_route'))
    db.session.delete(vacant_group)
    db.session.commit()
    flash('Asociación eliminada correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('horas_bp.group_view_route', group_id=vacant_group.id_grupo))


# Función para actualizar las horas de una plaza asignada a un grupo
def update_hours():
    form = FormPlazaGrupoUpdate()
    if form.validate_on_submit():
        vacant_group_id = form.vacant_group_id.data
        vacant_group = PlazaGrupo.get_with_id(vacant_group_id)
        vacant_group.horas = form.hours.data
        db.session.commit()
        flash('Horas actualizadas correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('horas_bp.group_view_route', group_id=vacant_group.id_grupo))
    flash('Se produjo un error al actualizar las horas', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('horas_bp.index_route'))


def assign_hours_ajax():
    hours = request.form.get('hours')
    vacant_group_id = request.form.get('vacant_group_id')

    # Validar que se recibieron ambos valores
    if hours is None or vacant_group_id is None:
        return jsonify({'error': 'Se requieren las horas y el ID del grupo vacante.'}), 400

    # Validar que las horas sean un número entero positivo
    try:
        hours = int(hours)
        if hours <= 0:
            return jsonify({'error': 'Las horas deben ser un número entero positivo.'}), 400
    except ValueError:
        return jsonify({'error': 'Las horas deben ser un número entero positivo.'}), 400

    # Validar que el ID del grupo vacante sea un número entero positivo
    try:
        vacant_group_id = int(vacant_group_id)
        if vacant_group_id <= 0:
            return jsonify({'error': 'El ID del grupo vacante debe ser un número entero positivo.'}), 400
    except ValueError:
        return jsonify({'error': 'El ID del grupo vacante debe ser un número entero positivo.'}), 400

    vacat_group = PlazaGrupo.get_with_id(vacant_group_id)
    if vacat_group is None:
        return jsonify({'error': 'No existe la asociación de plaza-grupo con el ID recibido.'}), 400
    vacat_group.horas = hours
    db.session.commit()

    # info = Grupo.get_all_json_hours(vacat_group.grupo.curso_asignatura.curso.id)
    result = 'Horas asignadas correctamente'
    # return jsonify({'message': result, 'info': info})
    return jsonify({'message': result})
