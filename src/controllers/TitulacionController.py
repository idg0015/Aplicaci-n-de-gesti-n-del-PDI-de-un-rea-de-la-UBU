from flask import render_template, redirect, url_for, abort
from forms import FormTitulacion
from models.Titulacion import Titulacion


def index():
    titulaciones = Titulacion.get_all_json()
    return render_template('titulaciones/index.html', titulaciones=titulaciones)


def add():
    formulario = FormTitulacion()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        url = formulario.url.data
        id_centro = formulario.centro.data

        titulacion = Titulacion(nombre=nombre, abreviatura=abreviatura, url=url, id_centro=id_centro)
        titulacion.save()
        return redirect(url_for('titulacion_bp.index'))
    return render_template('titulaciones/form.html', form=formulario)


def update(id_titulacion):
    titulacion = Titulacion.get_titulacion(id_titulacion)
    if titulacion is None:
        abort(404)
    formulario = FormTitulacion(obj=titulacion)
    formulario.submit.label.text = 'Modificar'
    if formulario.validate_on_submit():
        titulacion.nombre = formulario.nombre.data
        titulacion.abreviatura = formulario.abreviatura.data
        titulacion.url = formulario.url.data
        titulacion.id_centro = formulario.centro.data
        titulacion.save()
        return redirect(url_for('titulacion_bp.index'))
    return render_template('titulaciones/form.html', form=formulario)


def delete(id_titulacion):
    titulacion = Titulacion.get_titulacion(id_titulacion)
    if titulacion is None:
        abort(404)
    titulacion.delete()
    return redirect(url_for('titulacion_bp.index'))
