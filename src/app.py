from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
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
from utils.db import db

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa2\xff\xc0\x97\xeb%\x81\xa6L\xe3\x9aK\x19y\xa6(\xcf\xa2^c\xe1?\x8bG'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://zbsq33h1pl7u7b5t:dlgdfhx30l58iktl@j5zntocs2dn6c3fj.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/hg67y1474ek9zjug"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLAlchemy(app)
db.init_app(app)
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
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
