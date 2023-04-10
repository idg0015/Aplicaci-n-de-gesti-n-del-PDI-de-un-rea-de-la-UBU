from flask import Blueprint

from controllers.DocenteController import index

docente_bp = Blueprint('docente_bp', __name__)

docente_bp.route('/', methods=['GET'])(index)
