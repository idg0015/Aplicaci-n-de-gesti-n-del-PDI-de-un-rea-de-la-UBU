from utils.db import db


class PlazaGrupo(db.Model):
    __tablename__ = 'plaza_grupo'

    id = db.Column(db.Integer, primary_key=True)
    horas = db.Column(db.Integer)
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupo.id', ondelete='CASCADE'), nullable=False)
    id_plaza = db.Column(db.Integer, db.ForeignKey('plaza.id', ondelete='CASCADE'), nullable=False)

    grupo = db.relationship('Grupo', back_populates="plazas")
    plaza = db.relationship('Plaza', back_populates="grupos")

    # Relación entre horas y créditos. 1 crédito = 25 horas
    ECTS_HOUR = 25

    def to_dict(self):
        if self.plaza.docente is None:
            teacher = self.plaza.nombre,
            anual_capacity = self.plaza.tipo_contrato.capacidad_anual
        else:
            teacher = self.plaza.docente.nombre + ' ' + self.plaza.docente.apellidos
            anual_capacity = self.plaza.tipo_contrato.capacidad_anual - self.plaza.docente.reducciones

        return {
            'id': self.id,
            'hours': self.horas,
            'teacher': teacher,
            'in_other_groups': str(self.plaza.hours_in_other_groups(self.id,
                                                                    self.grupo.curso_asignatura.curso.id)) + ' h = ' +
                               str(self.plaza.hours_in_other_groups(self.id,
                                                                    self.grupo.curso_asignatura.curso.id) / PlazaGrupo.ECTS_HOUR)
                               + ' ECTS',
            'annual_capacity': anual_capacity,
            'group_id': self.id_grupo,
            'vacant_id': self.id_plaza
        }

    @staticmethod
    def get_all_json():
        vacants_groups = PlazaGrupo.query.all()
        return [vg.to_dict() for vg in vacants_groups]

    @staticmethod
    def get_vacancies_group_json(id_group):
        vacants_groups = PlazaGrupo.query.filter_by(id_grupo=id_group).all()
        return [vg.to_dict() for vg in vacants_groups]

    @staticmethod
    def get_with_id(vancat_group_id):
        return PlazaGrupo.query.filter_by(id=vancat_group_id).first()

    @staticmethod
    def get_with_vacant_and_group_id(vacant_id, group_id):
        return PlazaGrupo.query.filter_by(id_plaza=vacant_id, id_grupo=group_id).first()
