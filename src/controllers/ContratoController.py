from flask import render_template, redirect, url_for, abort, flash, session

from forms import FormContrato
from models.Contrato import TipoContrato
from models.Docente import Docente


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('contrato_bp.index_route'), 'Tipos de contrato'),
    ]
    contratos = TipoContrato.get_all_json()

    return render_template('contratos/index.html', tipos_contrato=contratos, breadcrumbs=breadcrumbs)


def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('contrato_bp.index_route'), 'Tipos de contrato'),
        ('', 'Añadir tipo de contrato'),
    ]
    formulario = FormContrato()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        capacidad_anual = formulario.capacidad_anual.data
        contrato = TipoContrato(nombre=nombre, abreviatura=abreviatura, capacidad_anual=capacidad_anual)
        contrato.save()
        flash('Tipo de contrato añadido correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('contrato_bp.index_route'))
    return render_template('contratos/form.html', form=formulario, breadcrumbs=breadcrumbs)


def update(id_contrato):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('contrato_bp.index_route'), 'Tipos de contrato'),
        ('', 'Modificar tipo de contrato ' + str(id_contrato)),
    ]
    contrato = TipoContrato.get_contrato(id_contrato)
    if contrato is None:
        abort(404)
    formulario = FormContrato(obj=contrato)
    formulario.submit.label.text = 'Modificar'
    if formulario.validate_on_submit():
        contrato.nombre = formulario.nombre.data
        contrato.abreviatura = formulario.abreviatura.data
        contrato.capacidad_anual = formulario.capacidad_anual.data
        contrato.save()
        flash('Tipo de contrato modificado correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('contrato_bp.index_route'))
    return render_template('contratos/form.html', form=formulario, breadcrumbs=breadcrumbs)


def delete(id_contrato):
    contrato = TipoContrato.get_contrato(id_contrato)
    if contrato is None:
        abort(404)
    contrato.delete()
    flash('Tipo de contrato eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('contrato_bp.index_route'))
