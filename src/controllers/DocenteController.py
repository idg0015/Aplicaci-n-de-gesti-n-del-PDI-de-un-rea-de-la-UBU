from flask import render_template, redirect, url_for, abort, flash, request, session

from forms import FormDocente, FormDocenteUpdate
from models.Docente import Docente


def index():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('docente_bp.index_route'), 'Docentes')
    ]
    docentes = Docente.get_all_json()

    return render_template('docentes/index.html', docentes=docentes, breadcrumbs=breadcrumbs)


def add():
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('docente_bp.index_route'), 'Docentes'),
        ('', 'Añadir docente')
    ]
    formulario = FormDocente()
    if formulario.validate_on_submit():
        if Docente.get_docente_email(formulario.email.data) is not None:
            flash('Ya existe un docente con ese email', 'alert alert-danger alert-dismissible fade show')
            return render_template('docentes/form.html', form=formulario, breadcrumbs=breadcrumbs)

        nombre = formulario.nombre.data
        apellidos = formulario.apellidos.data
        email = formulario.email.data
        reducciones = formulario.reducciones.data
        modification = formulario.modification_flag.data
        read = formulario.read_flag.data
        docente = Docente(nombre=nombre, apellidos=apellidos, email=email, reducciones=reducciones,
                          modification_flag=modification, read_flag=read)
        docente.save()
        flash('Docente añadido correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('docente_bp.index_route'))

    return render_template('docentes/form.html', form=formulario, breadcrumbs=breadcrumbs)


def add_modal():
    formulario = FormDocente()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        apellidos = formulario.apellidos.data
        email = formulario.email.data
        reducciones = formulario.reducciones.data
        modification = formulario.modification_flag.data
        read = formulario.read_flag.data
        docente = Docente(nombre=nombre, apellidos=apellidos, email=email, reducciones=reducciones,
                          modification_flag=modification, read_flag=read)
        docente.save()
        flash('Docente añadido correctamente', 'alert alert-success alert-dismissible fade show')
        flash(
            'Puede cerrar la ventana si no quiere añadir más docentes. El docente nuevo puede ser seleccionado desde el campo "Docente"',
            'alert alert-primary alert-dismissible fade show')
        formulario = FormDocente()
    return render_template('docentes/modal-form.html', form=formulario)


def update(id_docente):
    breadcrumbs = [
        ('/', 'Inicio'),
        (url_for('docente_bp.index_route'), 'Docentes'),
        ('', 'Modificar docente ' + str(id_docente))
    ]
    docente = Docente.get_docente(id_docente)
    if docente is None:
        abort(404)
    formulario = FormDocenteUpdate(obj=docente)
    formulario.submit.label.text = 'Modificar'
    flag = False

    if formulario.validate_on_submit():
        docente.nombre = formulario.nombre.data
        docente.apellidos = formulario.apellidos.data
        docente.email = formulario.email.data
        docente.reducciones = formulario.reducciones.data
        if id_docente != session['user_id']:
            docente.modification_flag = formulario.modification_flag.data
            docente.read_flag = formulario.read_flag.data
        else:
            if docente.modification_flag != formulario.modification_flag.data or docente.read_flag != formulario.read_flag.data:
                flash('¡No puedes modificar tus propios permisos!', 'alert alert-danger alert-dismissible fade show')
                flag = True
        if docente.modification_flag and not docente.read_flag:
            docente.read_flag = True
        docente.save()

        if flag:
            flash('El resto de datos se han modificado correctamente',
                  'alert alert-success alert-dismissible fade show')
        else:
            flash('Docente modificado correctamente', 'alert alert-success alert-dismissible fade show')
        return redirect(url_for('docente_bp.index_route'))
    return render_template('docentes/form.html', form=formulario, breadcrumbs=breadcrumbs, update=True)


def delete(id_docente):
    if id_docente == session['user_id']:
        flash('¡No puedes eliminarte a ti mismo!', 'alert alert-danger alert-dismissible fade show')
        return redirect(url_for('docente_bp.index_route'))

    docente = Docente.get_docente(id_docente)
    if docente is None:
        abort(404)
    docente.delete()
    flash('Docente eliminado correctamente', 'alert alert-success alert-dismissible fade show')
    return redirect(url_for('docente_bp.index_route'))


def get_docentes_ajax():
    texto = request.args.get('texto')
    return Docente.get_ajax(texto)
