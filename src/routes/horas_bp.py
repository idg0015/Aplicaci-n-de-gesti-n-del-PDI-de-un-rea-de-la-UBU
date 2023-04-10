from flask import Blueprint

from controllers.HorasController import index

horas_bp = Blueprint('horas_bp', __name__)

horas_bp.route('/', methods=['GET'])(index)
