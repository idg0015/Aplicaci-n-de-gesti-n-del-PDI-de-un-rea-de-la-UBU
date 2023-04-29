from flask import Blueprint

from controllers.PlazaController import *

plaza_bp = Blueprint('plaza_bp', __name__)

# Index
plaza_bp.route('/', methods=['GET'])(index)

# Creación
plaza_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
plaza_bp.route('/<int:id_plaza>/', methods=['GET', 'POST'])(update)

# Eliminación
plaza_bp.route('/eliminar/<int:id_plaza>/', methods=['GET'])(delete)
