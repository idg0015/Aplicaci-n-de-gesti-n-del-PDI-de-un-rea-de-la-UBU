from flask import Blueprint

from controllers.SiteController import *
from decorators import *

site_bp = Blueprint('site_bp', __name__)


@site_bp.route('/')
@token_required
@require_read_permission
def index_route():
    return index()


@site_bp.route('/login', methods=['GET', 'POST'])
def login_route():
    return login()


@site_bp.route('/logout')
@token_required
def logout_route():
    return logout()
