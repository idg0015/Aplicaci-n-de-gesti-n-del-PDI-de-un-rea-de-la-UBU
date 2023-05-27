from sqlalchemy import or_

from models.Docente import Docente
from utils.db import db


class Plaza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    rpt = db.Column(db.String(256), nullable=False)
    num_concursos_contratacion = db.Column(db.Integer, nullable=True)
    fecha_incorporacion = db.Column(db.Date, nullable=False)
    fecha_cese = db.Column(db.Date, nullable=True)

    # Relación con docente
    id_docente = db.Column(db.Integer, db.ForeignKey('docente.id', ondelete='CASCADE'), nullable=True)
    docente = db.relationship('Docente', back_populates='plazas')

    # Relación con área
    id_area = db.Column(db.Integer, db.ForeignKey('area.id', ondelete='CASCADE'), nullable=False)
    area = db.relationship('Area', back_populates='plazas')

    # Relación con tipos de contrato
    id_contrato = db.Column(db.Integer, db.ForeignKey('tipo_contrato.id', ondelete='CASCADE'), nullable=False)
    tipo_contrato = db.relationship('TipoContrato', back_populates='plazas')

    grupos = db.relationship('PlazaGrupo', back_populates='plaza', cascade='all, delete-orphan')

    def to_dict(self):
        docente = None
        if self.docente is not None:
            docente = self.docente.nombre + ' ' + self.docente.apellidos
        else:
            docente = '-'

        if self.fecha_cese is None:
            f_cese = '-'
        else:
            f_cese = self.fecha_cese.strftime("%d-%m-%Y")

        return {
            'id': self.id,
            'nombre': self.nombre,
            'rpt': self.rpt,
            'num_concursos_contratacion': self.num_concursos_contratacion,
            'fecha_incorporacion': self.fecha_incorporacion.strftime("%d-%m-%Y"),
            'fecha_cese': f_cese,
            'docente': docente,
            # 'area': self.area.nombre,
            'tipo_contrato': self.tipo_contrato.nombre
        }

    @staticmethod
    def get_all_json():
        plazas = Plaza.query.all()
        return [p.to_dict() for p in plazas]

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_plaza(id_plaza):
        return Plaza.query.get(id_plaza)

    @staticmethod
    def get_ajax(text):
        vacancies = Plaza.query.outerjoin(Docente).filter(
            or_(Plaza.nombre.ilike(f'%{text}%'),
                Docente.nombre.ilike(f'%{text}%'))
        ).all()

        results = []
        for vacant in vacancies:
            data = {
                'id': vacant.id,
                'text': vacant.nombre
            }
            if vacant.docente is not None:
                data['text'] += ': ' + vacant.docente.nombre + ' ' + vacant.docente.apellidos
            results.append(data)
        return results

    def hours_in_other_groups(self, group_id, course_id):
        hours = 0
        for group in self.grupos:
            if group.grupo.curso_asignatura.curso.id == course_id:
                if int(group.id) != int(group_id):
                    hours += group.horas
        return hours
