from flask import Blueprint
from controllers.DocenteController import *

docente_bp = Blueprint('docente_bp', __name__)

# Index
docente_bp.route('/', methods=['GET'])(index)

# Creación
docente_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
docente_bp.route('/<int:id_docente>/', methods=['GET', 'POST'])(update)

# Eliminación
docente_bp.route('/eliminar/<int:id_docente>/', methods=['GET'])(delete)
