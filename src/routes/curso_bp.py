from flask import Blueprint

from controllers.CursoController import *

curso_bp = Blueprint('curso_bp', __name__)

# Index
curso_bp.route('/', methods=['GET'])(index)

# Creación
curso_bp.route('/nuevo', methods=['GET', 'POST'])(add)
