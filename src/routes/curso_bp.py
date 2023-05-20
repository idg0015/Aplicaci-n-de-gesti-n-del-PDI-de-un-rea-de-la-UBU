from flask import Blueprint

from controllers.CursoController import *
from controllers.CursoAsignaturaController import gestion, delete_ca

curso_bp = Blueprint('curso_bp', __name__)

# Index
curso_bp.route('/', methods=['GET'])(index)

# Creación
curso_bp.route('/nuevo', methods=['GET', 'POST'])(add)

# Render sortable
curso_bp.route('/sortable', methods=['POST'])(render_sortable)

# Render sortable edit
curso_bp.route('/sortable-edit', methods=['POST'])(render_sortable_edit)

# Eliminar
curso_bp.route('/eliminar/<int:id_curso>', methods=['GET'])(delete)

# Duplicar
curso_bp.route('/duplicar/<int:id_curso>', methods=['GET'])(duplicate)

# Actualizar año
curso_bp.route('/actualizar-a', methods=['GET', 'POST'])(update_year)

# Edición
curso_bp.route('/<int:id_curso>', methods=['GET', 'POST'])(update)

# Gestión de asignaturas
curso_bp.route('/gestion/<int:id_curso_asignatura>', methods=['GET'])(gestion)

# Eliminar curso asignatura
curso_bp.route('/delete-ca/<int:id_curso_asignatura>', methods=['GET'])(delete_ca)
