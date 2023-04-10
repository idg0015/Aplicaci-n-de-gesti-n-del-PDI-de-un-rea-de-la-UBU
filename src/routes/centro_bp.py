from flask import Blueprint

from controllers.CentroController import index

centro_bp = Blueprint('centro_bp', __name__)

centro_bp.route('/', methods=['GET'])(index)
