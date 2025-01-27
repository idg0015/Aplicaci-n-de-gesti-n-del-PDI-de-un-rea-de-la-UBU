from flask import Blueprint

from controllers.DepartamentoController import *
from decorators import *

departamento_bp = Blueprint('departamento_bp', __name__)


# Index
@departamento_bp.route('/', methods=['GET'])
@token_required
@require_read_permission
def index_route():
    return index()


# Creación
@departamento_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def add_route():
    return add()


# Edición
@departamento_bp.route('/<int:id_departamento>/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def update_route(id_departamento):
    return update(id_departamento)


# Eliminación
@departamento_bp.route('/eliminar/<int:id_departamento>/', methods=['GET'])
@token_required
@require_modification_permission
def delete_route(id_departamento):
    return delete(id_departamento)


# Ajax get departamentos
@departamento_bp.route('/ajax/get_departamentos', methods=['GET'])
@token_required
@require_modification_permission
def get_departamentos_ajax_route():
    return get_departamentos_ajax()
