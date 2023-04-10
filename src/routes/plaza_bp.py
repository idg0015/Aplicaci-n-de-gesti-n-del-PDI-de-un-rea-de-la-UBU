from flask import Blueprint

from controllers.PlazaController import index

plaza_bp = Blueprint('plaza_bp', __name__)

plaza_bp.route('/', methods=['GET'])(index)
