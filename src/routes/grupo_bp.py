from flask import Blueprint

from controllers.GrupoController import *

grupo_bp = Blueprint('grupo_bp', __name__)

# Index
grupo_bp.route('/', methods=['GET'])(index)

# Get Cursos Asignaturas
grupo_bp.route('/cursos-asignaturas', methods=['POST'])(get_all_json)

# Get Horas
grupo_bp.route('/horas', methods=['POST'])(get_all_json_hours)

# Creación
grupo_bp.route('/nuevo/', methods=['POST'])(add)

# Eliminación
grupo_bp.route('/eliminar/<int:id_grupo>', methods=['GET'])(delete)
