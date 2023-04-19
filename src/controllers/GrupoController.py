from flask import render_template
from models.Grupo import Grupo


def index():
    return render_template('grupos/index.html')
