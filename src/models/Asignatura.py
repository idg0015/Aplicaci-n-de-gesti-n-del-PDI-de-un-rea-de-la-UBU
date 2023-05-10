from dataclasses import dataclass
from utils.db import db


class Asignatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
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
            "codigo": self.codigo,
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

    @staticmethod
    def get_asignatura(id_asignatura):
        return Asignatura.query.get(id_asignatura)

    @staticmethod
    def get_asignaturas_groupby_titulacion():
        asignaturas = Asignatura.query.all()
        asignaturas_groupby_titulacion = {}
        for a in asignaturas:
            if a.titulacion.nombre not in asignaturas_groupby_titulacion.keys():
                asignaturas_groupby_titulacion[a.titulacion.nombre] = []
            asignaturas_groupby_titulacion[a.titulacion.nombre].append(a)
        return asignaturas_groupby_titulacion

    @staticmethod
    def get_asignaturas_by_titulacion(id_titulacion):
        return Asignatura.query.filter_by(id_titulacion=id_titulacion).all()

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
