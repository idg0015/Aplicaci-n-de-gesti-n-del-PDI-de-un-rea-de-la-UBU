from flask import render_template
from models.Area import Area


def index():
    areas = Area.get_all_json()
    return render_template('areas/index.html', areas=areas)
