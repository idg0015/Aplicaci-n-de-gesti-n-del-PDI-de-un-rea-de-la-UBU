from flask import render_template, redirect, url_for, abort, flash

from forms import FormAsignatura
from models.Asignatura import Asignatura
from models.Abreviatura import Abreviatura


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('asignatura_bp.index_route'), 'Asignaturas'),
    ]

    asignaturas = Asignatura.get_all_json()
    return render_template('asignaturas/index.html', asignaturas=asignaturas, breadcrumbs=breadcrumbs)


def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('asignatura_bp.index_route'), 'Asignaturas'),
        ('', 'Añadir asignatura'),
    ]
    formulario = FormAsignatura()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        codigo = formulario.codigo.data
        tipo = formulario.tipo.data
        creditos_teoria = formulario.creditos_teoria.data
        creditos_practica = formulario.creditos_practica.data
        curso = formulario.curso.data
        semestre = formulario.semestre.data
        id_titulacion = formulario.titulacion.data

        asignatura = Asignatura(codigo=codigo, nombre=nombre, tipo=tipo, id_titulacion=id_titulacion,
                                creditos_teoria=creditos_teoria,
                                creditos_practica=creditos_practica, curso=curso, semestre=semestre)
        asignatura.save()

        # Guardo las abreviaturas
        for abreviatura in formulario.abreviatura.data:
            abreviatura = Abreviatura(abreviatura=abreviatura, id_asignatura=asignatura.id)
            abreviatura.save()
        flash('Asignatura añadida correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('asignatura_bp.index_route'))
    return render_template('asignaturas/form.html', form=formulario, breadcrumbs=breadcrumbs)


def update(id_asignatura):
    asignatura = Asignatura.get_asignatura(id_asignatura)

    if asignatura is None:
        abort(404)

    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('asignatura_bp.index_route'), 'Asignaturas'),
        ('', 'Modificar asignatura: ' + asignatura.nombre),
    ]

    formulario = FormAsignatura(obj=asignatura)
    formulario.submit.label.text = 'Modificar'

    if formulario.validate_on_submit():
        asignatura.codigo = formulario.codigo.data
        asignatura.nombre = formulario.nombre.data
        asignatura.tipo = formulario.tipo.data
        asignatura.creditos_teoria = formulario.creditos_teoria.data
        asignatura.creditos_practica = formulario.creditos_practica.data
        asignatura.curso = formulario.curso.data
        asignatura.semestre = formulario.semestre.data
        asignatura.save()

        # abreviaturas_actuales = asignatura.abreviaturas
        # Comparo si las abreviaturas han cambiado
        abreviaturas_actuales = [m.abreviatura for m in asignatura.abreviaturas]
        if set(abreviaturas_actuales) != set(formulario.abreviatura.data):
            for abreviatura in formulario.abreviatura.data:
                if abreviatura not in abreviaturas_actuales:
                    abreviatura = Abreviatura(abreviatura=abreviatura, id_asignatura=asignatura.id)
                    abreviatura.save()
            for abreviatura in abreviaturas_actuales:
                if abreviatura not in formulario.abreviatura.data:
                    abreviatura = Abreviatura.get_abreviatura(abreviatura, id_asignatura)
                    abreviatura.delete()

        flash('Asignatura modificada correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('asignatura_bp.index_route'))
    abreviaturas_actuales = [a.abreviatura for a in asignatura.abreviaturas]
    formulario.abreviatura.choices = abreviaturas_actuales
    formulario.abreviatura.data = abreviaturas_actuales
    return render_template('asignaturas/form.html', form=formulario, breadcrumbs=breadcrumbs)


def delete(id_asignatura):
    asignatura = Asignatura.get_asignatura(id_asignatura)
    if asignatura is None:
        abort(404)
    asignatura.delete()
    flash('Asignatura eliminada correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('asignatura_bp.index_route'))
