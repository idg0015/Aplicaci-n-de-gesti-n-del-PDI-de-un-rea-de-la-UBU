from flask import render_template, flash, redirect, url_for

from forms import FormGrupo
from models.CursoAsignatura import CursoAsignatura
from models.Grupo import Grupo
from utils.db import db


def gestion(id_curso_asignatura):
    curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
    grupos = Grupo.get_all_json(curso_asignatura.id)
    form = FormGrupo()

    return render_template('cursos/gestion.html', curso_asignatura=curso_asignatura, grupos=grupos, form=form)


def delete_ca(id_curso_asignatura):
    curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
    if curso_asignatura is not None:
        if curso_asignatura.grupos:
            flash('No se puede eliminar la asignatura del curso porque tiene grupos asociados. Elimine antes los grupos',
                  'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('grupo_bp.index'))
        db.session.delete(curso_asignatura)
        db.session.commit()
        flash('Asignatura eliminada del curso correctamente', 'alert alert-success alert-dismissible fade show')
    else:
        flash('Asignatura no encontrada en el curso', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('grupo_bp.index'))
