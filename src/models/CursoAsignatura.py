from enum import Enum

from models.Grupo import Tipo
from utils.db import db


class Modalidad(Enum):
    Presencial = 'Presencial'
    Ingles = 'Inglés'
    Online = 'Online'


class CursoAsignatura(db.Model):
    __tablename__ = 'curso_asignatura'

    id = db.Column(db.Integer, primary_key=True)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id', ondelete='CASCADE'), nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id', ondelete='CASCADE'), nullable=False)

    # Cuando se cree, se duplicará el registro por cada modalidad rellena
    modalidad = db.Column(db.String(256), nullable=False)
    num_alumnos_previstos = db.Column(db.Integer, nullable=False)
    num_grupos_teoricos_previstos = db.Column(db.Integer, nullable=False)
    num_grupos_practicos_previstos = db.Column(db.Integer, nullable=False)

    # Relaciones
    curso = db.relationship('Curso', back_populates='asignaturas')
    asignatura = db.relationship('Asignatura', back_populates='cursos')
    grupos = db.relationship('Grupo', back_populates='curso_asignatura', cascade='all, delete')

    @staticmethod
    def get_with_id(id_curso_asignatura):
        return CursoAsignatura.query.filter_by(id=id_curso_asignatura).first()

    @staticmethod
    def get_curso_asignatura(id_asignatura, id_curso):
        return CursoAsignatura.query.filter_by(id_asignatura=id_asignatura, id_curso=id_curso).all()

    @staticmethod
    def get_all(course_id):
        return CursoAsignatura.query.filter_by(id_curso=course_id).all()

    @staticmethod
    def get_all_json(id_curso):
        curso_asignaturas = CursoAsignatura.query.filter_by(id_curso=id_curso).all()
        return [ca.to_dict() for ca in curso_asignaturas]

    def num_grupos_teoricos(self):
        return len([g for g in self.grupos if g.tipo == Tipo.Teorico.value])

    def num_grupos_practicos(self):
        return len([g for g in self.grupos if g.tipo == Tipo.Practico.value])

    def to_dict(self):
        return {
            'id': self.id,
            'asignatura': self.asignatura.nombre,
            'modalidad': self.modalidad,
            'num_alumnos_previstos': self.num_alumnos_previstos,
            'num_grupos_teoricos_previstos': self.num_grupos_teoricos_previstos,
            'num_grupos_practicos_previstos': self.num_grupos_practicos_previstos,
            'num_grupos_teoricos': self.num_grupos_teoricos(),
            'num_grupos_practicos': self.num_grupos_practicos()
        }
