from flask import Flask, render_template

from models.Centro import Centro
from models.Docente import Docente
from models.Plaza import Plaza
from models.Titulacion import Titulacion
from routes.centro_bp import centro_bp
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

db.init_app(app)
migrate.init_app(app, db)
with app.app_context():
    db.create_all()


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


@app.route('/')
def index():
    n_centros = Centro.query.count()
    n_titulaciones = Titulacion.query.count()
    n_docentes = Docente.query.count()
    n_plazas = Plaza.query.count()
    return render_template('index.html', n_centros=n_centros, n_titulaciones=n_titulaciones, n_docentes=n_docentes, n_plazas=n_plazas)


if __name__ == '__main__':
    app.run()
