from flask import render_template

from forms import FormGrupo
from models.CursoAsignatura import CursoAsignatura
from models.Grupo import Grupo


def gestion(id_curso_asignatura):
    curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
    grupos = Grupo.get_all_json(curso_asignatura.id)
    form = FormGrupo()

    return render_template('cursos/gestion.html', curso_asignatura=curso_asignatura, grupos=grupos, form=form)
