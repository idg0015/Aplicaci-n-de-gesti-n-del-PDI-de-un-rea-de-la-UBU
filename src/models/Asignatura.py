from dataclasses import dataclass
from utils.db import db


class Asignatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    tipo = db.Column(db.String(256), nullable=False)
    creditos_teoria = db.Column(db.Integer, nullable=False)
    creditos_practica = db.Column(db.Integer, nullable=False)
    curso = db.Column(db.String(80), nullable=False)
    semestre = db.Column(db.String(80), nullable=False)

    # Relación con su titulación
    id_titulacion = db.Column(db.Integer, db.ForeignKey('titulacion.id', ondelete='CASCADE'), nullable=False)
    titulacion = db.relationship('Titulacion', back_populates='asignaturas')

    # Relación con los cursos
    cursos = db.relationship('CursoAsignatura', back_populates='asignatura')

    # Relación con sus abreviaturas
    abreviaturas = db.relationship('Abreviatura', back_populates='asignatura')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "titulacion": self.titulacion.nombre,
            "creditos_teoria": self.creditos_teoria,
            "creditos_practica": self.creditos_practica,
            "curso": self.curso,
            "semestre": self.semestre,
            "abreviaturas": [a.abreviatura+" " for a in self.abreviaturas]
        }

    @staticmethod
    def get_all_json():
        asignaturas = Asignatura.query.all()
        return [a.to_dict() for a in asignaturas]
