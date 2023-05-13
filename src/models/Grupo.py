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
    plazas = db.relationship('PlazaGrupo', back_populates='grupo')
    curso_asignatura = db.relationship("CursoAsignatura", back_populates="grupos")



