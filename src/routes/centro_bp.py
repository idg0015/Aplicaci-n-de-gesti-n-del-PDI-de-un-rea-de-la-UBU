from flask import Blueprint

from controllers.CentroController import *
from decorators import *

centro_bp = Blueprint('centro_bp', __name__)


# Index
@centro_bp.route('/', methods=['GET'])
@token_required
@require_read_permission
def index_route():
    return index()


# Creación
@centro_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def add_route():
    return add()


# Edición
@centro_bp.route('/<int:id_centro>/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def update_route(id_centro):
    return update(id_centro)


# Eliminación
@centro_bp.route('/eliminar/<int:id_centro>/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def delete_route(id_centro):
    return delete(id_centro)


# View
@centro_bp.route('/centro/<int:id_centro>/', methods=['GET'])
@token_required
@require_read_permission
def view_route(id_centro):
    return view(id_centro)
