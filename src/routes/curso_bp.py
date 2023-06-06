from flask import Blueprint

from controllers.CursoController import *
from controllers.CursoAsignaturaController import gestion, delete_ca, edit_ca
from decorators import token_required

curso_bp = Blueprint('curso_bp', __name__)


# Index
@curso_bp.route('/', methods=['GET'])
@token_required
def index_route():
    return index()


# Creación
@curso_bp.route('/nuevo', methods=['GET', 'POST'])
@token_required
def add_route():
    return add()


# Render sortable
@curso_bp.route('/sortable', methods=['POST'])
@token_required
def render_sortable_route():
    return render_sortable()


# Render sortable edit
@curso_bp.route('/sortable-edit', methods=['POST'])
@token_required
def render_sortable_edit_route():
    return render_sortable_edit()


# Eliminar
@curso_bp.route('/eliminar/<int:id_curso>', methods=['GET'])
@token_required
def delete_route(id_curso):
    return delete(id_curso)


# Duplicar
@curso_bp.route('/duplicar', methods=['POST'])
@token_required
def duplicate_route():
    return duplicate()


# Actualizar año
@curso_bp.route('/actualizar-a', methods=['GET', 'POST'])
@token_required
def update_year_route():
    return update_year()


# Edición
@curso_bp.route('/<int:id_curso>', methods=['GET', 'POST'])
@token_required
def update_route(id_curso):
    return update(id_curso)


# Gestión de asignaturas
@curso_bp.route('/gestion/<int:id_curso_asignatura>', methods=['GET'])
@token_required
def gestion_route(id_curso_asignatura):
    return gestion(id_curso_asignatura)


# Eliminar curso asignatura
@curso_bp.route('/delete-ca/<int:id_curso_asignatura>', methods=['GET'])
@token_required
def delete_ca_route(id_curso_asignatura):
    return delete_ca(id_curso_asignatura)


# Editar curso asignatura
@curso_bp.route('/edit-ca/<int:id_curso_asignatura>', methods=['POST'])
@token_required
def edit_ca_route(id_curso_asignatura):
    return edit_ca(id_curso_asignatura)
