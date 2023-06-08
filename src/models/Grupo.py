from enum import Enum
from utils.db import db


class Tipo(Enum):
    Teorico = 'Teórico'
    Practico = 'Práctico'


# Debe estar después de la clase Tipo
from models.CursoAsignatura import CursoAsignatura


class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    tipo = db.Column(db.String(256), nullable=False)

    id_curso_asignatura = db.Column(db.Integer, db.ForeignKey('curso_asignatura.id', ondelete='CASCADE'),
                                    nullable=False)
    plazas = db.relationship('PlazaGrupo', back_populates='grupo', cascade='all, delete-orphan')
    curso_asignatura = db.relationship("CursoAsignatura", back_populates="grupos")

    # Variable utilizada para las opciones del formulario
    Tipos = [('Teórico', 'Teórico'), ('Práctico', 'Práctico')]

    @staticmethod
    def get_with_id(group_id):
        return Grupo.query.filter_by(id=group_id).first()

    @staticmethod
    def get_all_json(course_subject_id):
        groups = Grupo.query.filter_by(id_curso_asignatura=course_subject_id).order_by('nombre').all()
        return [g.to_dict() for g in groups]

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'plazas': [p.to_dict() for p in self.plazas]
        }

    def dict_vacancies(self):
        total_data = {}
        for i, vacant_group in enumerate(self.plazas):
            if vacant_group.plaza is None:
                total_data[i] = {
                    'teacher': '-',
                    'hours': '-',
                    'total_hours': '-',
                    'vacant_group_id': '-',
                    'teacher_id': '-',
                }
            else:
                total_h_course = vacant_group.plaza.hours_in_course(vacant_group.grupo.curso_asignatura.curso.id)
                if vacant_group.plaza.docente is not None:
                    total_data[i] = {
                        'teacher': vacant_group.plaza.docente.nombre + " " + vacant_group.plaza.docente.apellidos,
                        'hours': vacant_group.horas,
                        'total_hours': str(total_h_course) + '/' + str(
                            vacant_group.plaza.tipo_contrato.capacidad_anual - vacant_group.plaza.docente.reducciones),
                        'vacant_group_id': vacant_group.id,
                        'teacher_id': vacant_group.plaza.docente.id,
                    }
                else:
                    total_data[i] = {
                        'teacher': vacant_group.plaza.nombre,
                        'hours': vacant_group.horas,
                        'total_hours': str(total_h_course) + '/' + str(
                            vacant_group.plaza.tipo_contrato.capacidad_anual - vacant_group.plaza.docente.reducciones),
                        'vacant_group_id': vacant_group.id,
                        'teacher_id': '-',
                    }
        return total_data

    def to_dict_hours(self):
        vacancies = self.dict_vacancies()
        hours = []
        teachers = []
        total_hours = []
        vacant_group_ids = []
        teachers_ids = []
        for i in range(3):
            if i < len(vacancies):
                if i == 2 and len(vacancies) > 3:
                    total_h = 0
                    for j in range(len(vacancies)):
                        if j >= 2:
                            total_h += vacancies[j]['hours']
                    hours.append(total_h)
                    # Cuidado si se cambia el contenido, se usa en el index.html de grupos para comparación:
                    teachers.append('. . .')
                    total_hours.append('-')
                    # Cuidado si se cambia el contenido, se usa en el index.html de grupos para comparación:
                    vacant_group_ids.append('. . .')
                    teachers_ids.append('-')
                else:
                    hours.append(vacancies[i]['hours'])
                    teachers.append(vacancies[i]['teacher'])
                    total_hours.append(vacancies[i]['total_hours'])
                    vacant_group_ids.append(vacancies[i]['vacant_group_id'])
                    teachers_ids.append(vacancies[i]['teacher_id'])
            else:
                hours.append('-')
                teachers.append('-')
                total_hours.append('-')
                vacant_group_ids.append('-')
                teachers_ids.append('-')

        return {
            'group_id': self.id,
            'group_name': self.nombre,
            'subject_name': self.curso_asignatura.asignatura.nombre,
            'degree': self.curso_asignatura.asignatura.titulacion.nombre,
            'semester': self.curso_asignatura.asignatura.semestre,
            'hours_1': hours[0],
            'vacant_group_id_1': vacant_group_ids[0],
            'total_hours_1': total_hours[0],
            'teacher_1': teachers[0],
            'hours_2': hours[1],
            'vacant_group_id_2': vacant_group_ids[1],
            'total_hours_2': total_hours[1],
            'teacher_2': teachers[1],
            'hours_3': hours[2],
            'vacant_group_id_3': vacant_group_ids[2],
            'total_hours_3': total_hours[2],
            'teacher_3': teachers[2],
            'teacher_id_1': teachers_ids[0],
            'teacher_id_2': teachers_ids[1],
            'teacher_id_3': teachers_ids[2],
        }

    @staticmethod
    def get_all_json_hours(course_id):
        courses_subjects = CursoAsignatura.get_all(course_id)
        groups = []
        for course_subject in courses_subjects:
            groups += course_subject.grupos
        return [g.to_dict_hours() for g in groups]
