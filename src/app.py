import subprocess
from urllib.parse import urlparse

import pymysql
from flask import Flask, render_template, send_file, session
from flask_session import Session

from decorators import token_required, require_modification_permission
from models.Docente import Docente
from routes.centro_bp import centro_bp
from routes.site_bp import site_bp
from routes.titulacion_bp import titulacion_bp
from routes.area_bp import area_bp
from routes.asignatura_bp import asignatura_bp
from routes.curso_bp import curso_bp
from routes.grupo_bp import grupo_bp
from routes.docente_bp import docente_bp
from routes.plaza_bp import plaza_bp
from routes.contrato_bp import contrato_bp
from routes.departamento_bp import departamento_bp
from routes.horas_bp import horas_bp
from utils.db import db, migrate
import os

app = Flask(__name__)
env = os.environ.get('FLASK_ENV', 'development')
if env == 'production':
    app.config.from_object('config.production.ProductionConfig')
else:
    app.config.from_object('config.development.DevelopmentConfig')

# Configuración de Flask-Session
app.config['SESSION_SQLALCHEMY'] = db
app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_USE_SIGNER'] = True

db.init_app(app)
migrate.init_app(app, db)
with app.app_context():
    db.create_all()

server_session = Session(app)

app.register_blueprint(site_bp)
app.register_blueprint(centro_bp, url_prefix='/centros')
app.register_blueprint(titulacion_bp, url_prefix='/titulaciones')
app.register_blueprint(area_bp, url_prefix='/areas')
app.register_blueprint(asignatura_bp, url_prefix='/asignaturas')
app.register_blueprint(curso_bp, url_prefix='/cursos')
app.register_blueprint(grupo_bp, url_prefix='/grupos')
app.register_blueprint(docente_bp, url_prefix='/docentes')
app.register_blueprint(plaza_bp, url_prefix='/plazas')
app.register_blueprint(contrato_bp, url_prefix='/contratos')
app.register_blueprint(departamento_bp, url_prefix='/departamentos')
app.register_blueprint(horas_bp, url_prefix='/horas')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(403)
def page_not_found(error):
    return render_template('403.html'), 403

@app.context_processor
def inject_global_variables():
    is_admin = Docente.get_docente(session.get('user_id')).modification_flag
    return dict(is_admin=is_admin)


@app.route('/export_db', methods=['GET'])
@token_required
@require_modification_permission
def export_db():
    """Exportar la base de datos y descargar el archivo resultante"""
    uri = app.config['SQLALCHEMY_DATABASE_URI']
    parsed_uri = urlparse(uri)

    host = parsed_uri.hostname
    port = parsed_uri.port or 3306
    username = parsed_uri.username
    password = parsed_uri.password or ''
    database = parsed_uri.path[1:]

    connection = pymysql.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database
    )

    export_file = 'database_export.sql'
    with open(export_file, 'w') as file:
        cursor = connection.cursor()

        # Obtener la lista de tablas
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]

            # Obtener la estructura de la tabla
            cursor.execute(f"SHOW CREATE TABLE {table_name}")
            create_table = cursor.fetchone()[1]
            file.write(f"{create_table};\n\n")

            # Obtener los datos de la tabla
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            file.write(f"INSERT INTO {table_name} VALUES\n")
            for row in rows:
                values = [str(value) for value in row]
                file.write(f"({', '.join(values)}),\n")
            file.write(";\n\n")

    connection.close()
    print(f"Database exported to {export_file}")
    return send_file(export_file, as_attachment=True)


if __name__ == '__main__':
    app.run()
