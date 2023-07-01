from flask import render_template, redirect, url_for, abort, flash, request, session

from forms import FormArea
from models.Area import Area


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        ('', 'Áreas'),
    ]

    areas = Area.get_all_json()
    return render_template('areas/index.html', areas=areas, breadcrumbs=breadcrumbs)


def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('area_bp.index_route'), 'Áreas'),
        ('', 'Añadir área'),
    ]
    formulario = FormArea()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        id_departamento = formulario.departamento.data
        area = Area(nombre=nombre, abreviatura=abreviatura, id_departamento=id_departamento)
        area.save()
        flash('Área añadida correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('area_bp.index_route'))
    return render_template('areas/form.html', form=formulario, breadcrumbs=breadcrumbs)


def update(id_area):
    area = Area.get_area(id_area)

    if area is None:
        abort(404)

    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('area_bp.index_route'), 'Áreas'),
        ('', 'Modificar área: ' + area.nombre),
    ]

    formulario = FormArea(obj=area)
    formulario.submit.label.text = 'Modificar'
    if formulario.validate_on_submit():
        area.nombre = formulario.nombre.data
        area.abreviatura = formulario.abreviatura.data
        area.id_departamento = formulario.departamento.data
        area.save()
        flash('Área modificada correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('area_bp.index_route'))
    formulario.departamento.choices = [(area.departamento.id, area.departamento.nombre)]
    return render_template('areas/form.html', form=formulario, breadcrumbs=breadcrumbs)


def delete(id_area):
    area = Area.get_area(id_area)
    if area is None:
        abort(404)
    area.delete()
    flash('Área eliminada correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('area_bp.index_route'))


def get_areas_ajax():
    texto = request.args.get('texto')
    return Area.get_ajax(texto)
