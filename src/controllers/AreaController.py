from flask import render_template, redirect, url_for, abort

from forms import FormArea
from models.Area import Area


def index():
    areas = Area.get_all_json()
    return render_template('areas/index.html', areas=areas)


def add():
    formulario = FormArea()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        id_departamento = formulario.departamento.data
        area = Area(nombre=nombre, abreviatura=abreviatura, id_departamento=id_departamento)
        area.save()
        return redirect(url_for('area_bp.index'))
    return render_template('areas/form.html', form=formulario)


def update(id_area):
    area = Area.get_area(id_area)
    if area is None:
        abort(404)
    formulario = FormArea(obj=area)
    formulario.submit.label.text = 'Modificar'
    if formulario.validate_on_submit():
        area.nombre = formulario.nombre.data
        area.abreviatura = formulario.abreviatura.data
        area.id_departamento = formulario.departamento.data
        area.save()
        return redirect(url_for('area_bp.index'))
    return render_template('areas/form.html', form=formulario)


def delete(id_area):
    area = Area.get_area(id_area)
    if area is None:
        abort(404)
    area.delete()
    return redirect(url_for('area_bp.index'))
