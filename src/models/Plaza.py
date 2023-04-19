from utils.db import db


class Plaza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    rtp = db.Column(db.String(256), nullable=False)
    num_concursos_contratacion = db.Column(db.Integer, nullable=False)
    fecha_incorporacion = db.Column(db.String(256), nullable=False)
    fecha_cese = db.Column(db.String(256), nullable=False)

    # Relación con docente
    id_docente = db.Column(db.Integer, db.ForeignKey('docente.id', ondelete='CASCADE'), nullable=True)
    docente = db.relationship('Docente', back_populates='plazas')

    # Relación con área
    id_area = db.Column(db.Integer, db.ForeignKey('area.id', ondelete='CASCADE'), nullable=False)
    area = db.relationship('Area', back_populates='plazas')

    # Relación con tipos de contrato
    id_contrato = db.Column(db.Integer, db.ForeignKey('tipo_contrato.id', ondelete='CASCADE'), nullable=False)
    tipo_contrato = db.relationship('TipoContrato', back_populates='plazas')

    grupos = db.relationship('PlazaGrupo', back_populates='plaza')

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'rtp': self.rtp,
            'num_concursos_contratacion': self.num_concursos_contratacion,
            'fecha_incorporacion': self.fecha_incorporacion,
            'fecha_cese': self.fecha_cese,
            'docente': self.docente.nombre,
            # 'area': self.area.nombre,
            'tipo_contrato': self.tipo_contrato.nombre
        }

    @staticmethod
    def get_all_json():
        plazas = Plaza.query.all()
        return [p.to_dict() for p in plazas]
