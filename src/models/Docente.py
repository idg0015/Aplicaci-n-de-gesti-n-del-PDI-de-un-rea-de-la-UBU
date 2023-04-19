from utils.db import db


class Docente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    apellidos = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    reducciones = db.Column(db.Integer, nullable=False)

    # Relación con plaza
    plazas = db.relationship('Plaza', back_populates='docente')

    @staticmethod
    def get_all_json():
        docentes = Docente.query.all()
        return [d.to_dict() for d in docentes]

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'email': self.email,
            'reducciones': self.reducciones,
        }