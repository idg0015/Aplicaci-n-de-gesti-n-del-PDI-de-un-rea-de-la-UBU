from utils.db import db


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    abreviatura = db.Column(db.String(80), nullable=False)

    # Relacion con Departamento
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id', ondelete='CASCADE'), nullable=False)
    departamento = db.relationship('Departamento', back_populates="areas")

    # Relacion con Plaza
    plazas = db.relationship('Plaza', back_populates='area')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "abreviatura": self.abreviatura,
            "departamento": self.departamento.nombre
        }

    @staticmethod
    def get_all_json():
        areas = Area.query.all()
        return [a.to_dict() for a in areas]

    def get_area(id_area):
        return Area.query.get(id_area)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
