from flask import Blueprint

from controllers.PlazaController import *
from decorators import *

plaza_bp = Blueprint('plaza_bp', __name__)


# Index
@plaza_bp.route('/', methods=['GET'])
@token_required
@require_read_permission
def index_route():
    return index()


# Creación
@plaza_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def add_route():
    return add()


# Edición
@plaza_bp.route('/<int:id_plaza>/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def update_route(id_plaza):
    return update(id_plaza)


# Eliminación
@plaza_bp.route('/eliminar/<int:id_plaza>/', methods=['GET'])
@token_required
@require_modification_permission
def delete_route(id_plaza):
    return delete(id_plaza)


# Ajax get plazas
@plaza_bp.route('/ajax/get_plazas', methods=['GET'])
@token_required
@require_read_permission
def get_plazas_ajax_route():
    return get_plazas_ajax()
