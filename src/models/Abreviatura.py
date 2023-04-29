from utils.db import db


class Abreviatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abreviatura = db.Column(db.String(256), nullable=False)

    id_asignatura = db.Column(db.Integer, db.ForeignKey('asignatura.id', ondelete='CASCADE'), nullable=False)
    asignatura = db.relationship('Asignatura', back_populates='abreviaturas')

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Abreviatura.query.all()

    @staticmethod
    def get_abreviatura(abreviatura, id_asignatura):
        return Abreviatura.query.filter(Abreviatura.abreviatura == abreviatura,
                                        Abreviatura.id_asignatura == id_asignatura).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
