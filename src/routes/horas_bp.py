from flask import Blueprint

from controllers.HorasController import *

horas_bp = Blueprint('horas_bp', __name__)

horas_bp.route('/', methods=['GET'])(index)

# Grupo
horas_bp.route('/grupo/<int:group_id>', methods=['GET'])(group_view)

# Asignar horas
horas_bp.route('/asignar-horas', methods=['POST'])(assign_hours)
