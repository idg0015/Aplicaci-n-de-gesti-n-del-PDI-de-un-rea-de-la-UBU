from utils.db import db


class PlazaGrupo(db.Model):
    __tablename__ = 'plaza_grupo'

    id = db.Column(db.Integer, primary_key=True)
    horas = db.Column(db.Integer)
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupo.id', ondelete='CASCADE'), nullable=False)
    id_plaza = db.Column(db.Integer, db.ForeignKey('plaza.id', ondelete='CASCADE'), nullable=False)

    grupo = db.relationship('Grupo', back_populates="plazas")
    plaza = db.relationship('Plaza', back_populates="grupos")

    def to_dict(self):
        if self.plaza.docente is None:
            teacher = self.plaza.nombre,
        else:
            teacher = self.plaza.docente.nombre + ' ' + self.plaza.docente.apellidos

        return {
            'id': self.id,
            'hours': self.horas,
            'teacher': teacher,
            'hours_in_other_groups': self.plaza.hours_in_other_groups(self.id),
            'credits_in_other_groups': self.plaza.hours_in_other_groups(self.id)/25,
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

