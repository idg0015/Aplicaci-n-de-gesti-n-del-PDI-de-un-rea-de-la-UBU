from flask import render_template
from models.Titulacion import Titulacion


def index():
    titulaciones = Titulacion.get_all_json()
    return render_template('titulaciones/index.html', titulaciones=titulaciones)
