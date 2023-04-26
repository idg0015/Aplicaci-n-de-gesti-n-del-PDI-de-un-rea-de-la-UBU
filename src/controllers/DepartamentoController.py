from flask import render_template, redirect, url_for, abort

from forms import FormDepartamento
from models.Departamento import Departamento


def index():
    departamentos = Departamento.get_all_json()
    return render_template('departamentos/index.html', departamentos=departamentos)

def add():
    formulario = FormDepartamento()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        departamento = Departamento(nombre=nombre, abreviatura=abreviatura)
        departamento.save()
        return redirect(url_for('departamento_bp.index'))

    return render_template('departamentos/form.html', form=formulario)


def update(id_departamento):
    departamento = Departamento.get_departamento(id_departamento)
    if departamento is None:
        abort(404)
    formulario = FormDepartamento(obj=departamento)
    formulario.submit.label.text = 'Modificar'

    if formulario.validate_on_submit():
        departamento.nombre = formulario.nombre.data
        departamento.abreviatura = formulario.abreviatura.data
        departamento.save()

        return redirect(url_for('departamento_bp.index'))
    return render_template('departamentos/form.html', form=formulario)


def delete(id_departamento):
    departamento = Departamento.get_departamento(id_departamento)
    if departamento is None:
        abort(404)
    departamento.delete()
    return redirect(url_for('departamento_bp.index'))

