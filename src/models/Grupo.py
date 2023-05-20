from enum import Enum

from utils.db import db


class Tipo(Enum):
    Teorico = 'Teórico'
    Practico = 'Práctico'


class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    tipo = db.Column(db.String(256), nullable=False)

    id_curso_asignatura = db.Column(db.Integer, db.ForeignKey('curso_asignatura.id', ondelete='CASCADE'),
                                    nullable=False)
    plazas = db.relationship('PlazaGrupo', back_populates='grupo', cascade='all, delete-orphan')
    curso_asignatura = db.relationship("CursoAsignatura", back_populates="grupos")

    # Variable utilizada para las opciones del formulario
    Tipos = [('Teórico', 'Teórico'), ('Práctico', 'Práctico')]

    @staticmethod
    def get_with_id(id_grupo):
        return Grupo.query.filter_by(id=id_grupo).first()

    @staticmethod
    def get_all_json(id_curso_asignatura):
        grupos = Grupo.query.filter_by(id_curso_asignatura=id_curso_asignatura).order_by('nombre').all()
        return [g.to_dict() for g in grupos]

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'plazas': [p.to_dict() for p in self.plazas]
        }



