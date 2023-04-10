from flask import Blueprint

from controllers.ContratoController import index

contrato_bp = Blueprint('contrato_bp', __name__)

contrato_bp.route('/', methods=['GET'])(index)
