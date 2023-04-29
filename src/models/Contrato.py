from utils.db import db


class TipoContrato(db.Model):
    __tablename__ = 'tipo_contrato'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    abreviatura = db.Column(db.String(80), nullable=False)
    capacidad_anual = db.Column(db.Integer, nullable=False)

    plazas = db.relationship('Plaza', back_populates='tipo_contrato', cascade='all, delete-orphan')

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

    def get_contrato(id_contrato):
        return TipoContrato.query.get(id_contrato)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return TipoContrato.query.all()

    # @staticmethod
    # def get_ajax(texto):
    #     tiposContrato = TipoContrato.query.filter(TipoContrato.nombre.ilike(f'%{texto}%')).all()
    #
    #     results = []
    #     for tipoContrato in tiposContrato:
    #         data = {
    #             'id': tipoContrato.id,
    #             'text': tipoContrato.nombre
    #         }
    #         results.append(data)
    #     return results
