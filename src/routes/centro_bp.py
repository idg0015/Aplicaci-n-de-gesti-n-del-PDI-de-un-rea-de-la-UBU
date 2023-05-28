from flask import Blueprint

from controllers.CentroController import *

centro_bp = Blueprint('centro_bp', __name__)

# Index
centro_bp.route('/', methods=['GET'])(index)

# Creación
centro_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
centro_bp.route('/<int:id_centro>/', methods=['GET', 'POST'])(update)

# Eliminación
centro_bp.route('/eliminar/<int:id_centro>/', methods=['GET', 'POST'])(delete)

# View
centro_bp.route('/centro/<int:id_centro>/', methods=['GET'])(view)