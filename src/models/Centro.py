from dataclasses import dataclass
from utils.db import db


class Centro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    abreviatura = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    titulaciones = db.relationship("Titulacion", back_populates="centro")

    @staticmethod
    def get_all_json():
        centros = Centro.query.all()
        return [c.to_dict() for c in centros]

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "abreviatura": self.abreviatura,
            "email": self.email
        }
