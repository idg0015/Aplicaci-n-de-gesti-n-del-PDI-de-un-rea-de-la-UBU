from flask import Blueprint

from controllers.AreaController import *
from decorators import *

area_bp = Blueprint('area_bp', __name__)


# Index
@area_bp.route('/', methods=['GET'])
@token_required
@require_read_permission
def index_route():
    return index()


# Creación
@area_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def add_route():
    return add()


# Edición
@area_bp.route('/<int:id_area>/', methods=['GET', 'POST'])
@token_required
@require_modification_permission
def update_route(id_area):
    return update(id_area)


# Eliminación
@area_bp.route('/eliminar/<int:id_area>/', methods=['GET'])
@token_required
@require_modification_permission
def delete_route(id_area):
    return delete(id_area)


# Ajax get areas
@area_bp.route('/ajax/get_areas', methods=['GET'])
@token_required
@require_read_permission
def get_areas_ajax_route():
    return get_areas_ajax()
