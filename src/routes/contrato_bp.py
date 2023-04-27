from flask import Blueprint

from controllers.ContratoController import *

contrato_bp = Blueprint('contrato_bp', __name__)

# Index
contrato_bp.route('/', methods=['GET'])(index)

# Creación
contrato_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
contrato_bp.route('/<int:id_contrato>/', methods=['GET', 'POST'])(update)

# Eliminación
contrato_bp.route('/eliminar/<int:id_contrato>/', methods=['GET', 'POST'])(delete)
