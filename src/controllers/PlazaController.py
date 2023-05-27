from flask import render_template, redirect, url_for, flash, abort, request

from forms import FormPlaza
from models.Plaza import Plaza


def index():
    plazas = Plaza.get_all_json()
    return render_template('plazas/index.html', plazas=plazas)


def add():
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
        plaza = Plaza(nombre=nombre, rpt=rpt, num_concursos_contratacion=num_concursos_contratacion,
                      fecha_incorporacion=fecha_incorporacion, fecha_cese=fecha_cese, id_docente=id_docente,
                      id_area=id_area, id_contrato=id_contrato)
        flash('La plaza se ha creado correctamente', 'alert alert-success alert-dismissible fade show')
        plaza.save()
        return redirect(url_for('plaza_bp.index'))
    return render_template('plazas/form.html', form=formulario)


def update(id_plaza):
    plaza = Plaza.get_plaza(id_plaza)
    if plaza is None:
        abort(404)
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
        plaza.id_docente = id_docente
        plaza.id_area = formulario.area.data
        plaza.id_contrato = formulario.contrato.data
        plaza.save()
        flash('La plaza se ha modificado correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('plaza_bp.index'))
    formulario.area.choices = [(plaza.area.id, plaza.area.nombre)]  # Carga de la opción seleccionada
    if plaza.docente is not None:
        formulario.docente.choices = [
            (plaza.docente.id, plaza.docente.nombre + ' ' + plaza.docente.apellidos)]  # Carga de la opción seleccionada
    else:
        formulario.docente.choices = [(-1, 'Ninguno')]
    return render_template('plazas/form.html', form=formulario)


def delete(id_plaza):
    plaza = Plaza.get_plaza(id_plaza)
    if plaza is None:
        abort(404)
    plaza.delete()
    flash('La plaza se ha eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('plaza_bp.index'))


def get_plazas_ajax():
    text = request.args.get('text')
    return Plaza.get_ajax(text)
