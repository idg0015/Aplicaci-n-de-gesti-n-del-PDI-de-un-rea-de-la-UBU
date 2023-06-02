from flask import render_template, flash, redirect, url_for

from forms import FormGrupo, FormCursoAsignatura
from models.CursoAsignatura import CursoAsignatura
from models.Grupo import Grupo
from utils.db import db


def gestion(id_curso_asignatura):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('grupo_bp.index'), 'Grupos'),
        ('', 'Gestión')
    ]
    curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
    grupos = Grupo.get_all_json(curso_asignatura.id)
    form = FormGrupo()

    return render_template('cursos/gestion.html', curso_asignatura=curso_asignatura, grupos=grupos, form=form, breadcrumbs=breadcrumbs)


def delete_ca(id_curso_asignatura):
    curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
    if curso_asignatura is not None:
        if curso_asignatura.grupos:
            flash(
                'No se puede eliminar la asignatura del curso porque tiene grupos asociados. Elimine antes los grupos',
                'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('grupo_bp.index'))
        db.session.delete(curso_asignatura)
        db.session.commit()
        flash('Asignatura eliminada del curso correctamente', 'alert alert-success alert-dismissible fade show')
    else:
        flash('Asignatura no encontrada en el curso', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('grupo_bp.index'))


def edit_ca(id_curso_asignatura):
    form = FormCursoAsignatura()
    if form.validate_on_submit():
        curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
        if curso_asignatura is not None:
            curso_asignatura.num_alumnos_previstos = form.n_a_p.data
            curso_asignatura.num_grupos_teoricos_previstos = form.n_g_t.data
            curso_asignatura.num_grupos_practicos_previstos = form.n_g_p.data
            db.session.commit()
            flash('Asignatura del curso actualizada correctamente', 'alert alert-success alert-dismissible fade show')
        else:
            flash('Asignatura del curso no encontrada', 'alert alert-danger alert-dismissible fade show')
    else:
        flash('Formulario no válido', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('grupo_bp.index'))
