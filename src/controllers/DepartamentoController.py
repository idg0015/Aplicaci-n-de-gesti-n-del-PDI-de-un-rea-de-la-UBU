from flask import render_template, redirect, url_for, abort, flash, request, jsonify

from forms import FormDepartamento
from models.Departamento import Departamento


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('departamento_bp.index'), 'Departamentos'),
    ]
    departamentos = Departamento.get_all_json()
    return render_template('departamentos/index.html', departamentos=departamentos, breadcrumbs=breadcrumbs)

def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('departamento_bp.index'), 'Departamentos'),
        ('', 'Añadir departamento'),
    ]
    formulario = FormDepartamento()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        departamento = Departamento(nombre=nombre, abreviatura=abreviatura)
        departamento.save()
        flash('Departamento añadido correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('departamento_bp.index'))

    return render_template('departamentos/form.html', form=formulario, breadcrumbs=breadcrumbs)


def update(id_departamento):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('departamento_bp.index'), 'Departamentos'),
        ('', 'Modificar departamento ' + str(id_departamento)),
    ]
    departamento = Departamento.get_departamento(id_departamento)
    if departamento is None:
        abort(404)
    formulario = FormDepartamento(obj=departamento)
    formulario.submit.label.text = 'Modificar'

    if formulario.validate_on_submit():
        departamento.nombre = formulario.nombre.data
        departamento.abreviatura = formulario.abreviatura.data
        departamento.save()

        flash('Departamento modificado correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('departamento_bp.index'))
    return render_template('departamentos/form.html', form=formulario, breadcrumbs=breadcrumbs)


def delete(id_departamento):
    departamento = Departamento.get_departamento(id_departamento)
    if departamento is None:
        abort(404)
    departamento.delete()
    flash('Departamento eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('departamento_bp.index'))

def get_departamentos_ajax():
    texto = request.args.get('texto')
    return Departamento.get_ajax(texto)


