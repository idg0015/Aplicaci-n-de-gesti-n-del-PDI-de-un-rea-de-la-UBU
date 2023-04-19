from flask import render_template, jsonify
from models.Centro import Centro


def index():
    centros = Centro.get_all_json()
    return render_template('centros/index.html', centros=centros)

