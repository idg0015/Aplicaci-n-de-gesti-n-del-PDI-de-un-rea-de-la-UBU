from flask import Blueprint

from controllers.AsignaturaController import *
from decorators import *

asignatura_bp = Blueprint('asignatura_bp', __name__)


# Index
@asignatura_bp.route('/', methods=['GET'])
@token_required
@require_read_permission
def index_route():
    return index()


# Creación
@asignatura_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def add_route():
    return add()


# Edición
@asignatura_bp.route('/<int:id_asignatura>/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def update_route(id_asignatura):
    return update(id_asignatura)


# Eliminación
@asignatura_bp.route('/eliminar/<int:id_asignatura>/', methods=['GET'])
@token_required
@require_modification_permission
def delete_route(id_asignatura):
    return delete(id_asignatura)
