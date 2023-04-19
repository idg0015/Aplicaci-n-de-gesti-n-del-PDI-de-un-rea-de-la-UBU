from flask import render_template
from models.Contrato import TipoContrato


def index():
    contratos = TipoContrato.get_all_json()
    return render_template('contratos/index.html', tipos_contrato=contratos)
