from flask import Blueprint

from controllers.GrupoController import index

grupo_bp = Blueprint('grupo_bp', __name__)

grupo_bp.route('/', methods=['GET'])(index)
