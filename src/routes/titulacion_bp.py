from flask import Blueprint

from controllers.TitulacionController import index

titulacion_bp = Blueprint('titulacion_bp', __name__)

titulacion_bp.route('/', methods=['GET'])(index)
