from flask import Blueprint

from controllers.AsignaturaController import index

asignatura_bp = Blueprint('asignatura_bp', __name__)

asignatura_bp.route('/', methods=['GET'])(index)
