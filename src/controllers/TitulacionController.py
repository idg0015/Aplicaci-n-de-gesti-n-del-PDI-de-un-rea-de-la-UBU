from flask import render_template, redirect, url_for, abort, flash, request, session
from forms import FormTitulacion
from models.Docente import Docente
from models.Titulacion import Titulacion


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('titulacion_bp.index_route'), 'Titulaciones'),
    ]
    titulaciones = Titulacion.get_all_json()
    has_modification_permission = Docente.get_docente(session['user_id']).modification_flag
    return render_template('titulaciones/index.html', titulaciones=titulaciones, breadcrumbs=breadcrumbs,
                           has_modification_permission=has_modification_permission)


def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('titulacion_bp.index_route'), 'Titulaciones'),
        ('', 'Añadir titulación'),
    ]
    formulario = FormTitulacion()
    if formulario.validate_on_submit():
        codigo = formulario.codigo.data
        nombre = formulario.nombre.data
        abreviatura = formulario.abreviatura.data
        url = formulario.url.data
        id_centro = formulario.centro.data

        titulacion = Titulacion(codigo=codigo, nombre=nombre, abreviatura=abreviatura, url=url, id_centro=id_centro)
        titulacion.save()
        flash('Tiulación añadida correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('titulacion_bp.index_route'))
    return render_template('titulaciones/form.html', form=formulario, breadcrumbs=breadcrumbs)


def update(id_titulacion):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('titulacion_bp.index_route'), 'Titulaciones'),
        ('', 'Modificar titulación ' + str(id_titulacion)),
    ]
    titulacion = Titulacion.get_titulacion(id_titulacion)
    if titulacion is None:
        abort(404)
    formulario = FormTitulacion(obj=titulacion)
    formulario.submit.label.text = 'Modificar'
    if formulario.validate_on_submit():
        titulacion.codigo = formulario.codigo.data
        titulacion.nombre = formulario.nombre.data
        titulacion.abreviatura = formulario.abreviatura.data
        titulacion.url = formulario.url.data
        titulacion.id_centro = formulario.centro.data
        titulacion.save()
        flash('Titulación modificada correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('titulacion_bp.index_route'))
    return render_template('titulaciones/form.html', form=formulario, breadcrumbs=breadcrumbs)


def delete(id_titulacion):
    titulacion = Titulacion.get_titulacion(id_titulacion)
    if titulacion is None:
        abort(404)
    titulacion.delete()
    flash('Titulación eliminada correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('titulacion_bp.index_route'))


def get_titulaciones_ajax():
    texto = request.args.get('texto')
    return Titulacion.get_ajax(texto)


def view(id_titulacion):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('titulacion_bp.index_route'), 'Titulaciones'),
        ('', 'Información titulación ' + str(id_titulacion)),
    ]
    titulacion = Titulacion.get_titulacion(id_titulacion)
    asignaturas = titulacion.get_asignaturas()
    if titulacion is None:
        abort(404)
    has_modification_permission = Docente.get_docente(session['user_id']).modification_flag
    return render_template('titulaciones/view.html', titulacion=titulacion, asignaturas=asignaturas,
                           breadcrumbs=breadcrumbs, has_modification_permission=has_modification_permission)
