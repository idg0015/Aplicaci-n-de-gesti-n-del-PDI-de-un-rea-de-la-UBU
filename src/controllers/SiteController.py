import io
import re
import datetime
import pymysql
import requests
from flask import session, redirect, url_for, flash, render_template, make_response
from forms import FormLogin, FormDataBase
from models.Centro import Centro
from models.Docente import Docente
from models.Plaza import Plaza
from models.Titulacion import Titulacion
from utils.db import db


def index():
    n_centros = Centro.query.count()
    n_titulaciones = Titulacion.query.count()
    n_docentes = Docente.query.count()
    n_plazas = Plaza.query.count()
    return render_template('index.html', n_centros=n_centros, n_titulaciones=n_titulaciones, n_docentes=n_docentes,
                           n_plazas=n_plazas)


def login():
    form = FormLogin()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        docente = Docente.get_docente_email(username)
        if docente is None:
            flash('Usuario o contraseña incorrectos', 'alert alert-danger alert-dismissible fade show')
            return render_template('login.html', form=form)
        if docente.read_flag == 0 and docente.modification_flag == 0:
            flash('Usuario o contraseña incorrectos', 'alert alert-danger alert-dismissible fade show')
            return render_template('login.html', form=form)
        url_moodle = 'https://ubuvirtual.ubu.es/login/token.php'
        data = {
            'username': username,
            'password': password,
            'service': 'moodle_mobile_app'
        }
        response = requests.post(url_moodle, data=data)
        if response.status_code == 200:
            json_data = response.json()
            if not json_data.get('error'):
                session['token'] = json_data.get('token')
                session['user_id'] = docente.id
                return redirect(url_for('site_bp.index_route'))
            else:
                flash('Usuario o contraseña incorrectos', 'alert alert-danger alert-dismissible fade show')
        else:
            flash('Error en la comunicación con Moodle', 'alert alert-danger alert-dismissible fade show')

    return render_template('login.html', form=form)


def logout():
    session.pop('token', None)
    return redirect(url_for('site_bp.login_route'))


def export_db(host, port, username, password, database):
    connection = pymysql.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database
    )

    export_file = io.BytesIO()  # BytesIO para almacenar el archivo en memoria
    with export_file:
        cursor = connection.cursor()
        # Obtener la lista de tablas
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Generar script de exportación (datos de las tablas)
        for table in tables:
            table_name = table[0]

            if table_name == 'sessions' or table_name == 'alembic_version':
                continue

            # Obtener los datos de la tabla
            cursor.execute(f"SELECT * FROM `{table_name}`")
            rows = cursor.fetchall()

            if rows:
                column_names = [desc[0] for desc in cursor.description]
                export_file.write(f"INSERT INTO `{table_name}` ({', '.join(column_names)}) VALUES\n".encode())

                row_data = []
                for row in rows:
                    values = []
                    for value in row:
                        if value is None:
                            values.append("NULL")
                        elif isinstance(value, (str, bytes)):
                            values.append(f"'{value}'")
                        elif isinstance(value, (int, float)):
                            values.append(str(value))
                        elif isinstance(value, datetime.datetime):
                            values.append(f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'")
                        elif isinstance(value, datetime.date):
                            values.append(f"'{value.strftime('%Y-%m-%d')}'")
                        else:
                            values.append(str(value))
                    row_data.append(f"({', '.join(values)})")

                export_file.write(',\n'.join(row_data).encode())
                export_file.write(";\n\n".encode())

        export_file.seek(0)

        # Crear la respuesta y establecer el encabezado para descargar el archivo
        response = make_response(export_file.getvalue())
        response.headers.set('Content-Disposition', 'attachment', filename='database_export.sql')
        response.headers.set('Content-Type', 'application/octet-stream')

        return response


def import_db(host, port, username, password, database):
    """Importar la base de datos desde un archivo subido por el usuario"""
    connection = None
    form = FormDataBase()

    if form.validate_on_submit():
        sql_file = form.sql_file.data
        if sql_file.filename == '':
            flash('No se seleccionó ningún archivo.', 'alert alert-danger alert-dismissible fade show')
            return redirect(url_for('import_db'))

        try:
            sql_content = sql_file.read().decode('utf-8')
            connection = pymysql.connect(
                host=host,
                port=port,
                user=username,
                password=password,
                database=database,
                autocommit=False
            )
            connection.begin()  # Iniciar la transacción

            with connection.cursor() as cursor:
                cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
                cursor.execute('SET SQL_SAFE_UPDATES = 0')
                cursor.execute('SET AUTOCOMMIT = 0')

                # Cerrar la sesión de SQLAlchemy
                db.session.close()

                # Eliminar el contenido de todas las tablas para evitar problemas con las claves
                cursor.execute('SHOW TABLES')
                tables = cursor.fetchall()
                for table in tables:
                    table_name = table[0]
                    if table_name == 'sessions' or table_name == 'alembic_version':
                        continue
                    cursor.execute(f'TRUNCATE TABLE `{table_name}`')

                cursor.execute('SET SQL_SAFE_UPDATES = 1')
                cursor.execute('SET AUTOCOMMIT = 1')

                # Separar el contenido SQL en declaraciones individuales
                sql_statements = sql_content.split(';')

                # Ejecutar cada declaración SQL por separado
                for statement in sql_statements:
                    statement = statement.strip()  # Eliminar espacios en blanco
                    if statement:
                        if re.match(r"^\s*INSERT\s+", statement, re.IGNORECASE):  # Permitir solo INSERT y UPDATE
                            cursor.execute(statement)
                        else:
                            error_message = 'Se encontró una declaración SQL no permitida (Sólo se permiten INSERT y UPDATE).'
                            flash(error_message, 'alert alert-danger alert-dismissible fade show')
                            connection.rollback()
                            return redirect(url_for('import_db'))

                cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
                # Eliminar la sesión del usuario
                session.pop('token', None)
                session.pop('user_id', None)

                connection.commit()
                flash('Los datos se importaron correctamente.', 'alert alert-success alert-dismissible fade show')
                return redirect(url_for('import_db'))
        except pymysql.Error as e:
            error_message = f'Error al importar los datos: {str(e)}'
            flash(error_message, 'alert alert-danger alert-dismissible fade show')
            connection.rollback()
            return redirect(url_for('import_db'))
        except UnicodeDecodeError:
            error_message = 'Error al decodificar el archivo. Asegúrese de que el archivo sea un archivo SQL válido.'
            flash(error_message, 'alert alert-danger alert-dismissible fade show')
            connection.rollback()
            return redirect(url_for('import_db'))
        finally:
            if connection:
                connection.close()

    return render_template('import_db.html', form=form)
