from flask import render_template, redirect, url_for, flash, abort, request, session

from forms import FormPlaza
from models.Docente import Docente
from models.Plaza import Plaza


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('plaza_bp.index_route'), 'Plazas'),
    ]
    plazas = Plaza.get_all_json()

    return render_template('plazas/index.html', plazas=plazas, breadcrumbs=breadcrumbs)


def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('plaza_bp.index_route'), 'Plazas'),
        ('', 'Añadir plaza'),
    ]
    formulario = FormPlaza()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        rpt = formulario.rpt.data
        num_concursos_contratacion = formulario.num_concursos_contratacion.data
        fecha_incorporacion = formulario.fecha_incorporacion.data
        fecha_cese = formulario.fecha_cese.data
        id_docente = formulario.docente.data
        if id_docente == -1:
            id_docente = None
        id_area = formulario.area.data
        id_contrato = formulario.contrato.data

        # Compruebo si el docente tiene alguna plaza sin fecha de fin
        flag = True
        if id_docente is not None:
            docente = Docente.get_docente(id_docente)
            plazas_docente = docente.plazas
            if plazas_docente is not None:
                for plaza_docente in plazas_docente:
                    if plaza_docente.fecha_cese is None:
                        flag = False
        if flag:
            flash('La plaza se ha creado correctamente', 'alert alert-success alert-dismissible fade show')
        else:
            id_docente = None
            flash(
                'La plaza ha sido creada, pero no se ha asignado al docente seleccionado porque tiene una plaza sin fecha de cese',
                'alert alert-warning alert-dismissible fade show')

        plaza = Plaza(nombre=nombre, rpt=rpt, num_concursos_contratacion=num_concursos_contratacion,
                      fecha_incorporacion=fecha_incorporacion, fecha_cese=fecha_cese, id_docente=id_docente,
                      id_area=id_area, id_contrato=id_contrato)
        plaza.save()
        return redirect(url_for('plaza_bp.index_route'))
    return render_template('plazas/form.html', form=formulario, breadcrumbs=breadcrumbs)


def update(id_plaza):
    plaza = Plaza.get_plaza(id_plaza)
    if plaza is None:
        abort(404)

    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('plaza_bp.index_route'), 'Plazas'),
        ('', 'Modificar plaza: ' + plaza.nombre),
    ]

    formulario = FormPlaza(obj=plaza)
    formulario.submit.label.text = 'Modificar'
    if formulario.validate_on_submit():
        plaza.nombre = formulario.nombre.data
        plaza.rpt = formulario.rpt.data
        plaza.num_concursos_contratacion = formulario.num_concursos_contratacion.data
        plaza.fecha_incorporacion = formulario.fecha_incorporacion.data
        plaza.fecha_cese = formulario.fecha_cese.data
        id_docente = formulario.docente.data
        if id_docente == -1:
            id_docente = None
        # Compruebo si el docente tiene alguna plaza sin fecha de fin
        flag = True
        if id_docente is not None:
            docente = Docente.get_docente(id_docente)
            plazas_docente = docente.plazas
            if plazas_docente is not None:
                for plaza_docente in plazas_docente:
                    if plaza_docente.fecha_cese is None and plaza_docente.id != plaza.id:
                        flag = False
        if flag:
            plaza.id_docente = id_docente
        plaza.id_area = formulario.area.data
        plaza.id_contrato = formulario.contrato.data
        plaza.save()
        if flag:
            flash('La plaza se ha modificado correctamente', 'alert alert-success alert-dismissible fade show')
        else:
            flash(
                'La información de la plaza se ha modificado correctamente, pero el docente seleccionado ya tiene una plaza sin fecha de cese y no se le ha podido asignar esta plaza.',
                'alert alert-warning alert-dismissible fade show')
        return redirect(url_for('plaza_bp.index_route'))
    formulario.area.choices = [(plaza.area.id, plaza.area.nombre)]  # Carga de la opción seleccionada
    if plaza.docente is not None:
        formulario.docente.choices = [
            (plaza.docente.id, plaza.docente.nombre + ' ' + plaza.docente.apellidos)]  # Carga de la opción seleccionada
    else:
        formulario.docente.choices = [(-1, 'Ninguno')]
    return render_template('plazas/form.html', form=formulario, breadcrumbs=breadcrumbs)


def delete(id_plaza):
    plaza = Plaza.get_plaza(id_plaza)
    if plaza is None:
        abort(404)
    plaza.delete()
    flash('La plaza se ha eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('plaza_bp.index_route'))


def get_plazas_ajax():
    text = request.args.get('text')
    return Plaza.get_ajax(text)
