from utils.db import db


class TipoContrato(db.Model):
    __tablename__ = 'tipo_contrato'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    abreviatura = db.Column(db.String(80), nullable=False)
    capacidad_anual = db.Column(db.Integer, nullable=False)

    plazas = db.relationship('Plaza', back_populates='tipo_contrato')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "abreviatura": self.abreviatura,
            "capacidad_anual": self.capacidad_anual
        }

    @staticmethod
    def get_all_json():
        tiposContrato = TipoContrato.query.all()
        return [t.to_dict() for t in tiposContrato]