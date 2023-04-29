from flask import Blueprint

from controllers.AreaController import *

area_bp = Blueprint('area_bp', __name__)

# Index
area_bp.route('/', methods=['GET'])(index)

# Creación
area_bp.route('/nuevo/', methods=['GET', 'POST'])(add)

# Edición
area_bp.route('/<int:id_area>/', methods=['GET', 'POST'])(update)

# Eliminación
area_bp.route('/eliminar/<int:id_area>/', methods=['GET'])(delete)

# Ajax get areas
area_bp.route('/ajax/get_areas', methods=['GET'])(get_areas_ajax)
