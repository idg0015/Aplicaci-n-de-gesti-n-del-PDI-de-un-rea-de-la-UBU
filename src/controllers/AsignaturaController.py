from flask import render_template, redirect, url_for, abort, flash

from forms import FormAsignatura
from models.Asignatura import Asignatura
from models.Abreviatura import Abreviatura


def index():
    asignaturas = Asignatura.get_all_json()
    return render_template('asignaturas/index.html', asignaturas=asignaturas)


def add():
    formulario = FormAsignatura()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        tipo = formulario.tipo.data
        creditos_teoria = formulario.creditos_teoria.data
        creditos_practica = formulario.creditos_practica.data
        curso = formulario.curso.data
        semestre = formulario.semestre.data
        id_titulacion = formulario.titulacion.data

        asignatura = Asignatura(nombre=nombre, tipo=tipo, id_titulacion=id_titulacion, creditos_teoria=creditos_teoria,
                                creditos_practica=creditos_practica, curso=curso, semestre=semestre)
        asignatura.save()

        # Guardo las abreviaturas
        for abreviatura in formulario.abreviatura.data:
            abreviatura = Abreviatura(abreviatura=abreviatura, id_asignatura=asignatura.id)
            abreviatura.save()
        flash('Asignatura añadida correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('asignatura_bp.index'))
    return render_template('asignaturas/form.html', form=formulario)


def update(id_asignatura):
    asignatura = Asignatura.get_asignatura(id_asignatura)
    if asignatura is None:
        abort(404)
    formulario = FormAsignatura(obj=asignatura)
    formulario.submit.label.text = 'Modificar'
    abreviaturas_actuales = [a.abreviatura for a in asignatura.abreviaturas]
    formulario.abreviatura.choices = abreviaturas_actuales
    formulario.abreviatura.data = abreviaturas_actuales

    if formulario.validate_on_submit():
        asignatura.nombre = formulario.nombre.data
        asignatura.tipo = formulario.tipo.data
        asignatura.creditos_teoria = formulario.creditos_teoria.data
        asignatura.creditos_practica = formulario.creditos_practica.data
        asignatura.curso = formulario.curso.data
        asignatura.semestre = formulario.semestre.data
        # asignatura.save()

        abreviaturas_actuales = asignatura.abreviaturas
        # Comparo si las abreviaturas han cambiado
        ab = [m.abreviatura for m in abreviaturas_actuales]
        print(formulario.abreviatura.data)
        if set(abreviaturas_actuales) != set(formulario.abreviatura.data):
            for abreviatura in formulario.abreviatura.data:
                if abreviatura not in abreviaturas_actuales:
                    abreviatura = Abreviatura(abreviatura=abreviatura, id_asignatura=asignatura.id)
                    # abreviatura.save()

        flash('Asignatura modificada correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('asignatura_bp.index'))
    return render_template('asignaturas/form.html', form=formulario)


def delete(id_asignatura):
    asignatura = Asignatura.get_asignatura(id_asignatura)
    if asignatura is None:
        abort(404)
    asignatura.delete()
    flash('Asignatura eliminada correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('asignatura_bp.index'))
