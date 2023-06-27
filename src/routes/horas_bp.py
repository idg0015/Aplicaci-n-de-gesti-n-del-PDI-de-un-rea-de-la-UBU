from flask import Blueprint

from controllers.HorasController import *
from decorators import *

horas_bp = Blueprint('horas_bp', __name__)


@horas_bp.route('/', methods=['GET'])
@token_required
@require_read_permission
def index_route():
    return index()


# Grupo
@horas_bp.route('/grupo/<int:group_id>', methods=['GET'])
@token_required
@require_read_permission
def group_view_route(group_id):
    return group_view(group_id)


# Asignar horas
@horas_bp.route('/asignar-horas', methods=['POST'])
@token_required
@require_modification_permission
def assign_hours_route():
    return assign_hours()


# Asignar horas AJAX
@horas_bp.route('/asignar-horas-ajax', methods=['POST'])
@token_required
@require_modification_permission
def assign_hours_ajax_route():
    return assign_hours_ajax()


# Eliminar horas
@horas_bp.route('/eliminar/<int:vacant_group_id>', methods=['GET'])
@token_required
@require_modification_permission
def delete_route(vacant_group_id):
    return delete(vacant_group_id)


# Actualizar horas
@horas_bp.route('/editar', methods=['POST'])
@token_required
@require_modification_permission
def update_hours_route():
    return update_hours()
