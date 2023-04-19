from flask import render_template
from models.PlazaGrupo import PlazaGrupo


def index():
    return render_template('horas/index.html')
