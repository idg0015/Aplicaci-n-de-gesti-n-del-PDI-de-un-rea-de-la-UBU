from utils.db import db


class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    abreviatura = db.Column(db.String(80), nullable=False)

    # Relacion con Area
    areas = db.relationship('Area', back_populates="departamento")

    @staticmethod
    def get_all_json():
        departamentos = Departamento.query.all()
        return [d.to_dict() for d in departamentos]

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "abreviatura": self.abreviatura
        }

    @staticmethod
    def get_all():
        return Departamento.query.all()

    def get_departamento(id_departamento):
        return Departamento.query.get(id_departamento)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
