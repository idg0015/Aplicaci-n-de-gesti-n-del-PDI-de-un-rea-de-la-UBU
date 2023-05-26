from flask import render_template, redirect, url_for, flash

from forms import FormPlazaGrupo
from models.Curso import Curso
from models.Grupo import Grupo
from models.Plaza import Plaza
from models.PlazaGrupo import PlazaGrupo
from utils.db import db


def index():
    return render_template('horas/index.html', cursos=Curso.get_all())


def group_view(group_id):
    group = Grupo.get_with_id(group_id)
    vacancies = PlazaGrupo.get_vacancies_group_json(group_id)
    form = FormPlazaGrupo()
    return render_template('horas/view.html', plazas=vacancies, grupo=group, form=form)


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
            return redirect(url_for('horas_bp.group_view', group_id=group_id))

        vacant_group = PlazaGrupo(horas=hours, id_grupo=group_id, id_plaza=vacant_id)
        db.session.add(vacant_group)
        db.session.commit()
        flash('Horas asignadas correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('horas_bp.group_view', group_id=group_id))
