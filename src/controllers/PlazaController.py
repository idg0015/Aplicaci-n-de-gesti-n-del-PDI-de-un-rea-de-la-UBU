from flask import render_template
from models.Plaza import Plaza


def index():
    plazas = Plaza.get_all_json()
    return render_template('plazas/index.html', plazas=plazas)
