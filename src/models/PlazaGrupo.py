from utils.db import db


class PlazaGrupo(db.Model):
    __tablename__ = 'plaza_grupo'

    id = db.Column(db.Integer, primary_key=True)
    horas = db.Column(db.Integer)
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupo.id', ondelete='CASCADE'), nullable=False)
    id_plaza = db.Column(db.Integer, db.ForeignKey('plaza.id', ondelete='CASCADE'), nullable=False)

    grupo = db.relationship('Grupo', back_populates="plazas")
    plaza = db.relationship('Plaza', back_populates="grupos")

