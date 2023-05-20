from utils.db import db


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ano_inicio = db.Column(db.String(256), nullable=False)

    asignaturas = db.relationship('CursoAsignatura', back_populates='curso', cascade='all, delete-orphan')

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

    @staticmethod
    def get_curso(id_curso):
        return Curso.query.get(id_curso)

    @staticmethod
    def get_all():
        return Curso.query.all()

    def check_asignatura_modalidad(self, id_asignatura, modalidad):
        for curso_asignatura in self.asignaturas:
            if curso_asignatura.asignatura.id == id_asignatura and curso_asignatura.modalidad == modalidad:
                return True
        return False

    def save(self):
        db.session.add(self)
