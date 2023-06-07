from flask import Blueprint

from controllers.GrupoController import *
from decorators import *

grupo_bp = Blueprint('grupo_bp', __name__)


# Index
@grupo_bp.route('/', methods=['GET'])
@token_required
@require_read_permission
def index_route():
    return index()


# Get Cursos Asignaturas
@grupo_bp.route('/cursos-asignaturas', methods=['POST'])
@token_required
@require_read_permission
def get_all_json_route():
    return get_all_json()


# Get Horas
@grupo_bp.route('/horas', methods=['POST'])
@token_required
@require_read_permission
def get_all_json_hours_route():
    return get_all_json_hours()


# Creación
@grupo_bp.route('/nuevo/', methods=['POST'])
@token_required
@require_modification_permission
def add_route():
    return add()


# Eliminación
@grupo_bp.route('/eliminar/<int:id_grupo>', methods=['GET'])
@token_required
@require_modification_permission
def delete_route(id_grupo):
    return delete(id_grupo)
