from flask import Blueprint
from controllers.DocenteController import *
from decorators import token_required

docente_bp = Blueprint('docente_bp', __name__)


# Index
@docente_bp.route('/', methods=['GET'])
@token_required
def index_route():
    return index()


# Creación
@docente_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
def add_route():
    return add()


@docente_bp.route('/modal/nuevo/', methods=['GET', 'POST'])
@token_required
def add_modal_route():
    return add_modal()


# Edición
@docente_bp.route('/<int:id_docente>/', methods=['GET', 'POST'])
@token_required
def update_route(id_docente):
    return update(id_docente)


# Eliminación
@docente_bp.route('/eliminar/<int:id_docente>/', methods=['GET'])
@token_required
def delete_route(id_docente):
    return delete(id_docente)


# Ajax get docentes
@docente_bp.route('/ajax/get_docentes', methods=['GET'])
@token_required
def get_docentes_ajax_route():
    return get_docentes_ajax()
