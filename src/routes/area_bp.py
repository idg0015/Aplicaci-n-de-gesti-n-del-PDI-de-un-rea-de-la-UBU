from flask import Blueprint

from controllers.AreaController import index

area_bp = Blueprint('area_bp', __name__)

area_bp.route('/', methods=['GET'])(index)
