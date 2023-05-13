from utils.db import db


class Docente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    apellidos = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    reducciones = db.Column(db.Integer, nullable=False)

    # Relación con plaza
    plazas = db.relationship('Plaza', back_populates='docente', cascade='all, delete-orphan')

    @staticmethod
    def get_all_json():
        docentes = Docente.query.all()
        return [d.to_dict() for d in docentes]

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'email': self.email,
            'reducciones': self.reducciones,
        }

    @staticmethod
    def get_docente(id_docente):
        return Docente.query.get(id_docente)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_ajax(texto):
        docentes = Docente.query.filter((Docente.nombre.ilike(f'%{texto}%') | Docente.apellidos.ilike(f'%{texto}%')))

        results = []
        results.append({'id': -1, 'text': 'Ninguno'})
        for docente in docentes:
            data = {
                'id': docente.id,
                'text': docente.nombre + ' ' + docente.apellidos
            }
            results.append(data)
        return results
