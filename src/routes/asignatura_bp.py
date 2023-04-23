from flask import Blueprint

from controllers.AsignaturaController import *

asignatura_bp = Blueprint('asignatura_bp', __name__)

# Index
asignatura_bp.route('/', methods=['GET'])(index)

# Creación
asignatura_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
asignatura_bp.route('/<int:id_asignatura>/', methods=['GET', 'POST'])(update)

# Eliminación
asignatura_bp.route('/eliminar/<int:id_asignatura>/', methods=['GET'])(delete)
