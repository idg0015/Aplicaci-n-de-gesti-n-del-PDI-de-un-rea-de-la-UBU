import math
from flask import render_template, jsonify, request, flash, redirect, url_for
from forms import FormCurso, FormCursoUpdate, UpdateYearCursoForm
from models.Asignatura import Asignatura
from models.Curso import Curso
from models.CursoAsignatura import CursoAsignatura, Modalidad
from models.Grupo import Grupo, Tipo
from models.Plaza import Plaza
from models.PlazaGrupo import PlazaGrupo
from utils.db import db


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('curso_bp.index'), 'Cursos'),
    ]
    cursos = Curso.get_all_json()
    form = UpdateYearCursoForm()
    return render_template('cursos/index.html', cursos=cursos, form=form, breadcrumbs=breadcrumbs)


def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('curso_bp.index'), 'Cursos'),
        ('', 'Añadir curso'),
    ]
    formulario = FormCurso()
    if formulario.validate_on_submit():
        ano_inicio = formulario.ano_inicio.data
        if Curso.get_curso_by_year(ano_inicio) is not None:
            flash('Ya existe un curso con ese año de inicio', 'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('curso_bp.index'))
        curso = Curso(ano_inicio=ano_inicio)
        db.session.add(curso)
        db.session.commit()
        flash('Curso creado correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('curso_bp.update', id_curso=curso.id))
    return render_template('cursos/form-create.html', form=formulario, breadcrumbs=breadcrumbs)


def update(id_curso):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('curso_bp.index'), 'Cursos'),
        ('', 'Modificar curso ' + str(id_curso)),
    ]
    curso = Curso.get_curso(id_curso)
    formulario = FormCursoUpdate(obj=curso)
    list_asignaturas = list(set([str(curso_asignatura.id_asignatura) for curso_asignatura in curso.asignaturas]))
    # asignaturas_actuales = list(set([curso_asignatura.asignatura for curso_asignatura in curso.asignaturas]))

    if curso is None:
        flash('Curso no encontrado', 'alert alert-danger alert-dismissible fade show')
        return redirect(url_for('curso_bp.index'))
    if formulario.validate_on_submit():
        alumnos_presencial = formulario.n_a_p.data
        alumnos_ingles = formulario.n_a_i.data
        alumnos_online = formulario.n_a_o.data

        asignaturas_nuevas = formulario.id_asignaturas.data.split(',')
        # asignaturas_to_add = list(set(asignaturas_nuevas) - set(list_asignaturas))

        if len(asignaturas_nuevas) > 0:
            for id_asignatura in asignaturas_nuevas:
                if alumnos_presencial > 0:
                    if not curso.check_asignatura_modalidad(id_asignatura, Modalidad.Presencial.value):
                        create_relation(1, 1, id_asignatura, curso.id, alumnos_presencial, Modalidad.Presencial)
                if alumnos_ingles > 0:
                    if not curso.check_asignatura_modalidad(id_asignatura, Modalidad.Ingles.value):
                        create_relation(1, 1, id_asignatura, curso.id, alumnos_ingles, Modalidad.Ingles)
                if alumnos_online > 0:
                    if not curso.check_asignatura_modalidad(id_asignatura, Modalidad.Online.value):
                        create_relation(1, 1, id_asignatura, curso.id, alumnos_online, Modalidad.Online)

        db.session.commit()

        flash('Asignaturas y grupos añadidos correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('curso_bp.index'))

    # formulario.id_asignaturas.data = ','.join(
    #     set([str(curso_asignatura.id_asignatura) for curso_asignatura in curso.asignaturas]))
    return render_template('cursos/form-update.html', form=formulario, asig_actuales=[],
                           id_curso=id_curso, breadcrumbs=breadcrumbs)


def create_relation(n_g_t, n_g_p, id_asignatura, id_curso, alumnos, modalidad):
    curso_asignatura = CursoAsignatura(modalidad=modalidad.value,
                                       num_alumnos_previstos=alumnos,
                                       num_grupos_teoricos_previstos=n_g_t,
                                       num_grupos_practicos_previstos=n_g_p,
                                       id_curso=id_curso, id_asignatura=id_asignatura)
    db.session.add(curso_asignatura)
    db.session.flush()

    if n_g_t > 0:
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
        cursos_asignaturas = Curso.get_curso(request.form.get('id_curso')).asignaturas
        asignaturas_curso = []
        for curso_asignatura in cursos_asignaturas:
            asignaturas_curso.append(curso_asignatura.asignatura)
        asignaturas = Asignatura.get_asignaturas_by_titulacion_curso(request.form.get('id_titulacion'),
                                                                     request.form.get('curso'))
        return jsonify(render_template('cursos/sortable.html', asignaturas=asignaturas))


def render_sortable_edit():
    if request.method == "POST":
        cursos_asignaturas = Curso.get_curso(request.form.get('id_curso')).asignaturas
        asignaturas_curso = []
        for curso_asignatura in cursos_asignaturas:
            asignaturas_curso.append(curso_asignatura.asignatura)
        asignaturas = Asignatura.get_asignaturas_by_titulacion_curso(request.form.get('id_titulacion'),
                                                                     request.form.get('curso'))

        return jsonify(
            render_template('cursos/sortable.html', asignaturas=list(set(asignaturas) - set(asignaturas_curso))))


def delete(id_curso):
    curso = Curso.get_curso(id_curso)
    if curso is not None:
        if curso.asignaturas:
            flash('No se puede eliminar el curso porque tiene asignaturas asociadas',
                  'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('curso_bp.index'))
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
            cursos = Curso.get_all()
            flag = True
            for c in cursos:
                if int(c.ano_inicio) == int(form.year.data) and int(c.id) != int(form.id_curso.data):
                    flag = False

            if flag:
                db.session.commit()
                flash('Curso actualizado correctamente', 'alert alert-success alert-dismissible fade show')
            else:
                flash('No se puede modificar a ese año. Ya existe un curso con ese año de inicio',
                      'alert alert-danger alert-dismissible fade show')
        else:
            flash('Curso no encontrado', 'alert alert-danger alert-dismissible fade show')
        return redirect(url_for('curso_bp.index'))
    return render_template('cursos/modal.html', form=form)


def duplicate():
    if request.method == "POST":
        try:
            id_curso = request.form.get('id_curso')
            opcion = int(request.form.get('opcion'))
            curso = Curso.get_curso(id_curso)
            if curso is not None:
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
                        db.session.flush()
                        # Asignación de horas a plazas de un grupo
                        if opcion:
                            plazas = grupo.plazas
                            for plaza in plazas:
                                nueva_plaza = PlazaGrupo(id_grupo=nuevo_grupo.id, id_plaza=plaza.id_plaza,
                                                         horas=plaza.horas)
                                db.session.add(nueva_plaza)
                db.session.commit()
                data = {
                    'status': 'OK',
                    'message': 'Curso duplicado correctamente',
                    'data': Curso.get_all_json()
                }
                return jsonify(data)
            else:
                data = {
                    'status': 'ERROR',
                    'message': 'Curso no encontrado'
                }
                return jsonify(data)
        except Exception as e:
            db.session.rollback()
            data = {
                'status': 'ERROR',
                'message': 'Error al duplicar el curso: ' + str(e)
            }
            return jsonify(data)
