import math

from flask import render_template, request, flash, redirect, url_for

from forms import FormGrupo, FormCursoAsignatura
from models.Curso import Curso
from models.CursoAsignatura import CursoAsignatura, Modalidad
from models.Grupo import Grupo, Tipo
from utils.db import db


def index():
    """
    Muestra la vista principal de grupos
    """
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('grupo_bp.index_route'), 'Grupos'),
    ]
    # info = CursoAsignatura.get_all_json()
    form = FormCursoAsignatura()

    return render_template('grupos/index.html', cursos=Curso.get_all(), form=form, breadcrumbs=breadcrumbs)


def get_all_json():
    """
    Devuelve todos los CursoAsignatura de un cruso académico en un json
    """
    if request.method == "POST":
        return CursoAsignatura.get_all_json(request.form.get('id'))


def get_all_json_hours():
    """
    Devuelve todas las horas de los grupos en un json
    """
    if request.method == "POST":
        return Grupo.get_all_json_hours(request.form.get('id'))


def add():
    """
    Función que añade un grupo a una asignatura
    """
    form = FormGrupo()
    if form.validate_on_submit():
        curso_asignatura = CursoAsignatura.get_with_id(form.id_curso_asignatura.data)
        if curso_asignatura is not None:
            # Función encargada de la gestión automática de los nombres
            create_check_grupos(curso_asignatura.id, form.tipo.data)
        else:
            flash('Asignatura no encontrada en el curso', 'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('grupo_bp.index_route'))
        return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=curso_asignatura.id))
    flash('Error al añadir el grupo', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('grupo_bp.index_route'))


def create_check_grupos(id_curso_asignatura, tipo_nuevo):
    """
    Función que crea los grupos de una asignatura asignando de forma automática los nombres
    :param id_curso_asignatura: id del CursoAsignatura vinculado
    :param tipo_nuevo: Indica si el grupo es teórico o práctico
    """
    curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)
    n_g_t = curso_asignatura.num_grupos_teoricos()
    n_g_p = curso_asignatura.num_grupos_practicos()

    if tipo_nuevo == Tipo.Teorico.value:
        n_g_t += 1
        # Se calculan el número de grupos prácticos por grupo teórico y los restantes (que se añaden al primero)
        grupos_practicos_por_teorico = math.floor(n_g_p / n_g_t)
        grupos_practicos_restantes = n_g_p % n_g_t

        # Añado el nuevo grupo teórico
        nombre_nuevo = n_g_t
        # Segun la modalidad seleccionamos el código de grupo
        if curso_asignatura.modalidad == Modalidad.Ingles.value:
            nombre_nuevo = n_g_t + 79
        elif curso_asignatura.modalidad == Modalidad.Online.value:
            nombre_nuevo = n_g_t + 89

        nuevo = Grupo(nombre=nombre_nuevo, tipo=tipo_nuevo, id_curso_asignatura=curso_asignatura.id)
        flash('Grupo creado correctamente', 'alert alert-success alert-dismissible fade show')
        # Se añade a la sesión, pero no está hecho el commit!
        db.session.add(nuevo)

        # Llamada a la función encargada de gestionar los nombres de los grupos
        change_names(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes, False)

    elif tipo_nuevo == Tipo.Practico.value:
        if n_g_t > 0:
            n_g_p += 1
            grupos_practicos_por_teorico = math.floor(n_g_p / n_g_t)
            grupos_practicos_restantes = n_g_p % n_g_t
            change_names(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes, True)
        else:
            flash('No se puede crear un grupo práctico sin que exista al menos un grupo teórico',
                  'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=curso_asignatura.id))
    # Se hace el commit de la sesión
    db.session.commit()


def change_names(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes, new_p=False):
    """
    Función que gestiona los nombres de los grupos en la creación de nuevos grupos
    :param curso_asignatura: Objeto CursoAsignatura
    :param n_g_t: Nº de grupos teóricos
    :param grupos_practicos_por_teorico: Nº de grupos prácticos por grupo teórico
    :param grupos_practicos_restantes: Nº de grupos prácticos restantes
    :param new_p: Parámetro que indica si se está creando un grupo práctico (Por defecto False)
    """
    nombres_practicos = []
    for i in range(n_g_t):
        # Se calcula el primer nombre del grupo según la modalidad
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

        # Se calcula el último nombre previsto
        fin_nombre = inicio_nombre + num_grupos_practicos_teorico - 1

        # Se añaden los nombres a la lista
        for j in range(inicio_nombre, fin_nombre + 1):
            nombres_practicos.append(j)

    # Se recorren los grupos y se va cambiando el nombre según la lista generada anteriormente
    for grupo in curso_asignatura.grupos:
        if grupo.tipo == Tipo.Practico.value:
            grupo.nombre = nombres_practicos.pop(0)

    # Si se está creando un grupo práctico, se crea y se pone el nombre correspondiente al último grupo
    if new_p:
        nuevo = Grupo(nombre=nombres_practicos.pop(0), tipo=Tipo.Practico.value,
                      id_curso_asignatura=curso_asignatura.id)
        flash('Grupo creado correctamente', 'alert alert-success alert-dismissible fade show')
        # Se añade a la sesión, pero no está hecho el commit!
        db.session.add(nuevo)


def change_names_delete(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes):
    """
    Función similar a la anterior, pero para la eliminación de grupos. Se debe tener en cuenta al poner el nombre si es
    teórico o práctico
    :param curso_asignatura: Objeto CursoAsignatura
    :param n_g_t: Nº de grupos teóricos
    :param grupos_practicos_por_teorico: Nº de grupos prácticos por grupo teórico
    :param grupos_practicos_restantes: Nº de grupos prácticos restantes
    """
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
    """
    Función que elimina un grupo y llama a las otras funciones para cambiar los nombres de los grupos
    :param id_grupo: ID del grupo a eliminar
    :return:
    """
    grupo = Grupo.get_with_id(id_grupo)
    id_curso_asignatura = grupo.id_curso_asignatura
    if grupo is not None:
        # Lo eliminamos sin hacer el commit
        db.session.delete(grupo)
        # Se hace el flush para simular el commit, pero no son cambios efectivos
        db.session.flush()
        # Con el grupo "eliminado" recogemos los grupos del CursoAsignatura
        curso_asignatura = CursoAsignatura.get_with_id(id_curso_asignatura)

        n_g_t = curso_asignatura.num_grupos_teoricos()
        n_g_p = curso_asignatura.num_grupos_practicos()
        # Si el grupo no tiene plazas asociadas, se puede eliminar
        if len(grupo.plazas) == 0:
            # Si con el grupo "ya eliminado" hay 0 más grupos teóricos, se puede eliminar
            if n_g_t > 0:
                grupos_practicos_por_teorico = math.floor(n_g_p / n_g_t)
                grupos_practicos_restantes = n_g_p % n_g_t
                change_names_delete(curso_asignatura, n_g_t, grupos_practicos_por_teorico, grupos_practicos_restantes)
            else:
                # Si no hay grupos teóricos, hay que mirar si hay más grupos prácticos
                if len(curso_asignatura.grupos) > 0:
                    flash('No se puede eliminar el último grupo teórico si tiene grupos prácticos. Elimínelos antes',
                          'alert alert-danger alert-dismissible fade show')
                    return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=id_curso_asignatura))
        else:
            flash('No se puede eliminar un grupo con plazas asignadas',
                  'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=id_curso_asignatura))

        # Si no ha habido ninguna excepción, se puede eliminar y se hace el commit
        db.session.commit()
        flash('Grupo eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    else:
        flash('Grupo no encontrado', 'alert alert-danger alert-dismissible fade show')
    return redirect(url_for('curso_bp.gestion_route', id_curso_asignatura=id_curso_asignatura))
