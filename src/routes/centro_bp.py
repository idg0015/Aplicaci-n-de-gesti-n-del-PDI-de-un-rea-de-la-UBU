from flask import Blueprint

from controllers.CentroController import *
from decorators import token_required

centro_bp = Blueprint('centro_bp', __name__)


# Index
@centro_bp.route('/', methods=['GET'])
@token_required
def index_route():
    return index()


# Creación
@centro_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
def add_route():
    return add()


# Edición
@centro_bp.route('/<int:id_centro>/', methods=['GET', 'POST'])
@token_required
def update_route(id_centro):
    return update(id_centro)


# Eliminación
@centro_bp.route('/eliminar/<int:id_centro>/', methods=['GET', 'POST'])
@token_required
def delete_route(id_centro):
    return delete(id_centro)


# View
@centro_bp.route('/centro/<int:id_centro>/', methods=['GET'])
@token_required
def view_route(id_centro):
    return view(id_centro)
