from flask import Blueprint

from controllers.TitulacionController import *

titulacion_bp = Blueprint('titulacion_bp', __name__)

# Index
titulacion_bp.route('/', methods=['GET'])(index)

# Creación
titulacion_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
titulacion_bp.route('/<int:id_titulacion>/', methods=['GET', 'POST'])(update)

# Eliminación
titulacion_bp.route('/eliminar/<int:id_titulacion>/', methods=['GET'])(delete)
