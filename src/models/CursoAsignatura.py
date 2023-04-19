from utils.db import db


class CursoAsignatura(db.Model):
    __tablename__ = 'curso_asignatura'

    id = db.Column(db.Integer, primary_key=True)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id', ondelete='CASCADE'), nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id', ondelete='CASCADE'), nullable=False)
    # Cuando se cree, se duplicará el registro por cada modalidad rellenada
    modalidad = db.Column(db.String(256), nullable=False)
    num_alumnos_previstos = db.Column(db.Integer, nullable=False)
    num_grupos_teoricos_previstos = db.Column(db.Integer, nullable=False)
    num_grupos_practicos_previstos = db.Column(db.Integer, nullable=False)

    # Relaciones
    curso = db.relationship('Curso', back_populates='asignaturas')
    asignatura = db.relationship('Asignatura', back_populates='cursos')

