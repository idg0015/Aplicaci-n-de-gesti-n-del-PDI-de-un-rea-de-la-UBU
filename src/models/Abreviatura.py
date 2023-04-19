from utils.db import db


class Abreviatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abreviatura = db.Column(db.String(256), nullable=False)
    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id', ondelete='CASCADE'), nullable=False)
    asignatura = db.relationship('Asignatura', back_populates='abreviaturas')
