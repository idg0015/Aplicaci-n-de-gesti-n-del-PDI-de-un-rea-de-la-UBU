from flask import render_template


def index():
    return render_template('centros/index.html')