from flask import Blueprint

from controllers.CursoController import index

curso_bp = Blueprint('curso_bp', __name__)

curso_bp.route('/', methods=['GET'])(index)
