from utils.db import db


class Titulacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    abreviatura = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(256), nullable=False)

    id_centro = db.Column(db.Integer, db.ForeignKey('centro.id'), nullable=False)
    centro = db.relationship("Centro", back_populates="titulaciones")
    asignaturas = db.relationship("Asignatura", back_populates="titulacion")

    @staticmethod
    def get_all_json():
        titulaciones = Titulacion.query.all()
        return [t.to_dict() for t in titulaciones]

    def to_dict(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "abreviatura": self.abreviatura,
            "url": self.url,
            "centro": self.centro.nombre
        }

    @staticmethod
    def get_titulacion(id_titulacion):
        return Titulacion.query.get(id_titulacion)

    @staticmethod
    def get_all():
        return Titulacion.query.all()

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
