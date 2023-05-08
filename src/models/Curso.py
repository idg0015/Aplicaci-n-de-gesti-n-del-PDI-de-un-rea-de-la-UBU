from utils.db import db


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ano_inicio = db.Column(db.String(256), nullable=False)

    asignaturas = db.relationship('CursoAsignatura', back_populates='curso')

    @staticmethod
    def get_all_json():
        cursos = Curso.query.all()
        return [c.to_dict() for c in cursos]

    def to_dict(self):
        return {
            'id': self.id,
            'ano_inicio': self.ano_inicio,
            'ano_fin': int(self.ano_inicio) + 1,
        }

    def save(self):
        db.session.add(self)
        # db.session.commit()
