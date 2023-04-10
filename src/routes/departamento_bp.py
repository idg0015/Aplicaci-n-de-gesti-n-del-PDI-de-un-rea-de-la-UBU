from flask import Blueprint

from controllers.DepartamentoController import index

departamento_bp = Blueprint('departamento_bp', __name__)

departamento_bp.route('/', methods=['GET'])(index)
