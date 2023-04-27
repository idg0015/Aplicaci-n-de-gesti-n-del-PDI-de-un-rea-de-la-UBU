from flask import render_template, redirect, url_for, abort, flash

from forms import FormContrato
from models.Contrato import TipoContrato


def index():
    contratos = TipoContrato.get_all_json()
    return render_template('contratos/index.html', tipos_contrato=contratos)


def add():
    formulario = FormContrato()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        capacidad_anual = formulario.capacidad_anual.data
        contrato = TipoContrato(nombre=nombre, abreviatura=abreviatura, capacidad_anual=capacidad_anual)
        contrato.save()
        flash('Tipo de contrato añadido correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('contrato_bp.index'))
    return render_template('contratos/form.html', form=formulario)


def update(id_contrato):
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
        return redirect(url_for('contrato_bp.index'))
    return render_template('contratos/form.html', form=formulario)


def delete(id_contrato):
    contrato = TipoContrato.get_contrato(id_contrato)
    if contrato is None:
        abort(404)
    contrato.delete()
    flash('Tipo de contrato eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('contrato_bp.index'))
