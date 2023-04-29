from flask import render_template, redirect, url_for, abort, flash, request

from forms import FormDocente
from models.Docente import Docente


def index():
    docentes = Docente.get_all_json()
    return render_template('docentes/index.html', docentes=docentes)


def add():
    formulario = FormDocente()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        apellidos = formulario.apellidos.data
        email = formulario.email.data
        reducciones = formulario.reducciones.data
        docente = Docente(nombre=nombre, apellidos=apellidos, email=email, reducciones=reducciones)
        docente.save()
        flash('Docente añadido correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('docente_bp.index'))

    return render_template('docentes/form.html', form=formulario)


def add_modal():
    formulario = FormDocente()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        apellidos = formulario.apellidos.data
        email = formulario.email.data
        reducciones = formulario.reducciones.data
        docente = Docente(nombre=nombre, apellidos=apellidos, email=email, reducciones=reducciones)
        docente.save()
        flash('Docente añadido correctamente', 'alert alert-success alert-dismissible fade show')
        flash(
            'Puede cerrar la ventana si no quiere añadir más docentes. El docente nuevo puede ser seleccionado desde el campo "Docente"',
            'alert alert-primary alert-dismissible fade show')
        formulario = FormDocente()
    return render_template('docentes/modal-form.html', form=formulario)


def update(id_docente):
    docente = Docente.get_docente(id_docente)
    if docente is None:
        abort(404)
    formulario = FormDocente(obj=docente)
    formulario.submit.label.text = 'Modificar'

    if formulario.validate_on_submit():
        docente.nombre = formulario.nombre.data
        docente.apellidos = formulario.apellidos.data
        docente.email = formulario.email.data
        docente.reducciones = formulario.reducciones.data
        docente.save()

        flash('Docente modificado correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('docente_bp.index'))
    return render_template('docentes/form.html', form=formulario)


def delete(id_docente):
    docente = Docente.get_docente(id_docente)
    if docente is None:
        abort(404)
    docente.delete()
    flash('Docente eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('docente_bp.index'))


def get_docentes_ajax():
    texto = request.args.get('texto')
    return Docente.get_ajax(texto)
