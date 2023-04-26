from flask import Blueprint

from controllers.DepartamentoController import *

departamento_bp = Blueprint('departamento_bp', __name__)

# Index
departamento_bp.route('/', methods=['GET'])(index)

# Creación
departamento_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
departamento_bp.route('/<int:id_departamento>/', methods=['GET', 'POST'])(update)

# Eliminación
departamento_bp.route('/eliminar/<int:id_departamento>/', methods=['GET'])(delete)
