from flask import Blueprint

from controllers.GrupoController import *

grupo_bp = Blueprint('grupo_bp', __name__)

# Index
grupo_bp.route('/', methods=['GET'])(index)

# Gestión
grupo_bp.route('/gestion/<int:id_curso_asignatura>', methods=['GET'])(gestion)

# Get Cursos Asignaturas
grupo_bp.route('/cursos-asignaturas', methods=['POST'])(get_all_json)
