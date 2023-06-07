import requests
from flask import request, session, redirect, url_for, flash, render_template

from forms import FormLogin
from models.Centro import Centro
from models.Docente import Docente
from models.Plaza import Plaza
from models.Titulacion import Titulacion


def index():
    n_centros = Centro.query.count()
    n_titulaciones = Titulacion.query.count()
    n_docentes = Docente.query.count()
    n_plazas = Plaza.query.count()
    return render_template('index.html', n_centros=n_centros, n_titulaciones=n_titulaciones, n_docentes=n_docentes,
                           n_plazas=n_plazas)


def login():
    form = FormLogin()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        docente = Docente.get_docente_email(username)
        if docente is None:
            flash('Usuario o contraseña incorrectos', 'alert alert-danger alert-dismissible fade show')
            return render_template('login.html')
        url_moodle = 'https://ubuvirtual.ubu.es/login/token.php'
        data = {
            'username': username,
            'password': password,
            'service': 'moodle_mobile_app'
        }
        response = requests.post(url_moodle, data=data)
        if response.status_code == 200:
            json_data = response.json()
            if not json_data.get('error'):
                session['token'] = json_data.get('token')
                session['user_id'] = docente.id
                return redirect(url_for('site_bp.index_route'))
            else:
                flash('Usuario o contraseña incorrectos', 'alert alert-danger alert-dismissible fade show')
        else:
            flash('Error en la comunicación con Moodle', 'alert alert-danger alert-dismissible fade show')

    return render_template('login.html', form=form)


def logout():
    session.pop('token', None)
    return redirect(url_for('site_bp.login_route'))
