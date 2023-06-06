from flask import Blueprint

from controllers.ContratoController import *
from decorators import token_required

contrato_bp = Blueprint('contrato_bp', __name__)


# Index
@contrato_bp.route('/', methods=['GET'])
@token_required
def index_route():
    return index()


# Creación
@contrato_bp.route('/nuevo/', methods=['GET', 'POST'])
@token_required
def add_route():
    return add()


# Edición
@contrato_bp.route('/<int:id_contrato>/', methods=['GET', 'POST'])
@token_required
def update_route(id_contrato):
    return update(id_contrato)


# Eliminación
@contrato_bp.route('/eliminar/<int:id_contrato>/', methods=['GET', 'POST'])
@token_required
def delete_route(id_contrato):
    return delete(id_contrato)
